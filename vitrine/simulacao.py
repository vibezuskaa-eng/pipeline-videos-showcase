"""Implementações fictícias, só para a demonstração.

Nenhuma delas acessa arquivos, rede ou serviços: tudo é simulado em memória.
"""
import random

from .etapas import Analise, Edicao, Entrada, Fila, Publicacao
from .modelos import Conferencia, Estado, Item

DURACAO_MINIMA = 60.0


class EntradaSimulada(Entrada):
    def novos_itens(self) -> list[Item]:
        return [
            Item("exemplo-a", duracao_segundos=1800),
            Item("exemplo-b", duracao_segundos=0),  # inválido: será descartado
            Item("exemplo-c", duracao_segundos=900),
        ]


class AnaliseSimulada(Analise):
    def analisar(self, item: Item) -> Item:
        if item.duracao_segundos < DURACAO_MINIMA:
            item.estado = Estado.DESCARTADO
            item.registrar("descartado: conteúdo curto demais")
            return item
        item.titulo = f"Título gerado para {item.identificador}"
        item.descricao = "Descrição gerada automaticamente."
        item.estado = Estado.ANALISADO
        item.registrar("análise concluída")
        return item


class EdicaoSimulada(Edicao):
    def editar(self, item: Item) -> Item:
        item.versoes = ["formato-horizontal", "formato-vertical"]
        item.estado = Estado.EDITADO
        item.registrar(f"{len(item.versoes)} versões prontas")
        return item


class FilaSimulada(Fila):
    def __init__(self, limite_diario: int = 1):
        self.limite_diario = limite_diario

    def selecionar(self, itens: list[Item]) -> list[Item]:
        prontos = [i for i in itens if i.estado is Estado.EDITADO]
        for item in prontos[: self.limite_diario]:
            item.estado = Estado.NA_FILA
            item.registrar("selecionado para hoje")
        for item in prontos[self.limite_diario :]:
            item.registrar("aguardando próximo dia (limite diário)")
        return prontos[: self.limite_diario]


class PublicacaoSimulada(Publicacao):
    def __init__(self, semente: int = 7):
        self._sorteio = random.Random(semente)

    def enviar(self, item: Item) -> None:
        item.estado = Estado.ENVIADO
        item.registrar("enviado")

    def conferir(self, item: Item) -> Conferencia:
        # Simula o caso comum de o destino não salvar tudo na primeira vez.
        if self._sorteio.random() < 0.5:
            return Conferencia(False, "destino ainda sem descrição")
        return Conferencia(True)
