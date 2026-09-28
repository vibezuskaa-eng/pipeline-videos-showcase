"""Contratos de cada etapa. O sistema real implementa estas interfaces de
forma privada; aqui elas só descrevem o que cada etapa promete."""
from abc import ABC, abstractmethod

from .modelos import Conferencia, Item


class Entrada(ABC):
    @abstractmethod
    def novos_itens(self) -> list[Item]:
        """Itens prontos para processar (cópia concluída, ainda não vistos)."""


class Analise(ABC):
    @abstractmethod
    def analisar(self, item: Item) -> Item:
        """Preenche título e descrição a partir do conteúdo do item."""


class Edicao(ABC):
    @abstractmethod
    def editar(self, item: Item) -> Item:
        """Gera as versões finais do item."""


class Fila(ABC):
    @abstractmethod
    def selecionar(self, itens: list[Item]) -> list[Item]:
        """Escolhe o que sai agora, respeitando os limites do dia."""


class Publicacao(ABC):
    @abstractmethod
    def enviar(self, item: Item) -> None:
        """Envia o item ao destino."""

    @abstractmethod
    def conferir(self, item: Item) -> Conferencia:
        """Confirma no destino que o item ficou público e completo."""
