"""Encadeia as etapas. A regra central: só é "publicado" o que foi conferido."""
from .etapas import Analise, Edicao, Entrada, Fila, Publicacao
from .modelos import Estado, Item

TENTATIVAS_DE_CONFERENCIA = 3


class Orquestrador:
    def __init__(
        self,
        entrada: Entrada,
        analise: Analise,
        edicao: Edicao,
        fila: Fila,
        publicacao: Publicacao,
    ):
        self.entrada = entrada
        self.analise = analise
        self.edicao = edicao
        self.fila = fila
        self.publicacao = publicacao

    def executar(self) -> list[Item]:
        itens = [self.analise.analisar(i) for i in self.entrada.novos_itens()]
        itens = [
            self.edicao.editar(i) if i.estado is Estado.ANALISADO else i
            for i in itens
        ]
        for item in self.fila.selecionar(itens):
            self._publicar(item)
        return itens

    def _publicar(self, item: Item) -> None:
        self.publicacao.enviar(item)
        for tentativa in range(1, TENTATIVAS_DE_CONFERENCIA + 1):
            resultado = self.publicacao.conferir(item)
            if resultado.ok:
                item.estado = Estado.PUBLICADO
                item.registrar(f"conferido no destino (tentativa {tentativa})")
                return
            item.registrar(f"conferência falhou: {resultado.motivo}; completando")
        item.registrar("mantido na fila para nova tentativa")
