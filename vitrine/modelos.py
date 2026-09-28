"""Tipos de dados trocados entre as etapas do pipeline."""
from dataclasses import dataclass, field
from enum import Enum


class Estado(Enum):
    RECEBIDO = "recebido"
    ANALISADO = "analisado"
    EDITADO = "editado"
    NA_FILA = "na fila"
    ENVIADO = "enviado"
    PUBLICADO = "publicado"
    DESCARTADO = "descartado"


@dataclass
class Item:
    """Um conteúdo percorrendo o pipeline."""

    identificador: str
    duracao_segundos: float
    estado: Estado = Estado.RECEBIDO
    titulo: str = ""
    descricao: str = ""
    versoes: list[str] = field(default_factory=list)
    historico: list[str] = field(default_factory=list)

    def registrar(self, mensagem: str) -> None:
        self.historico.append(mensagem)


@dataclass
class Conferencia:
    """Resultado da checagem no destino depois do envio."""

    ok: bool
    motivo: str = ""
