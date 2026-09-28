"""Roda o fluxo completo com dados fictícios. Não lê, grava nem publica nada."""
from vitrine.orquestrador import Orquestrador
from vitrine.simulacao import (
    AnaliseSimulada,
    EdicaoSimulada,
    EntradaSimulada,
    FilaSimulada,
    PublicacaoSimulada,
)


def main() -> None:
    orquestrador = Orquestrador(
        EntradaSimulada(),
        AnaliseSimulada(),
        EdicaoSimulada(),
        FilaSimulada(limite_diario=1),
        PublicacaoSimulada(),
    )
    for item in orquestrador.executar():
        print(f"\n[{item.identificador}] estado final: {item.estado.value}")
        for passo in item.historico:
            print(f"  - {passo}")


if __name__ == "__main__":
    main()
