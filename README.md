# Pipeline de Conteúdo em Vídeo (vitrine)

> **Este repositório é uma vitrine de arquitetura, não um software funcional.**
> O sistema real é privado. Aqui estão só a estrutura, os contratos entre as
> etapas e uma demonstração que roda com dados fictícios.

## O que é

Um pipeline que leva um vídeo bruto até a publicação sem intervenção manual:

```
entrada ──► análise ──► edição ──► fila ──► publicação ──► conferência
```

| Etapa | Responsabilidade |
|---|---|
| **Entrada** | Detecta arquivos novos, espera a cópia terminar e descarta os inválidos |
| **Análise** | Extrai o conteúdo falado e gera os textos de apoio (título, descrição) |
| **Edição** | Monta as versões finais nos formatos exigidos por cada destino |
| **Fila** | Organiza o que sai e quando, respeitando limites diários |
| **Publicação** | Envia para cada destino |
| **Conferência** | Só considera publicado o que foi confirmado no destino |

## Princípios do projeto

- **Idempotência:** cada etapa pode ser repetida sem gerar duplicatas.
- **Conferência antes de concluir:** um envio só sai da fila quando o destino
  confirma que ficou público e completo, e não quando a tela "parece" certa.
- **Falha isolada:** um arquivo com problema é separado e registrado, e os
  demais seguem.
- **Uma instância por recurso:** travas impedem que dois processos disputem o
  mesmo destino.
- **Observabilidade:** cada decisão fica registrada em log, com o motivo.

## Estrutura

```
vitrine/
├── modelos.py        # tipos de dados trocados entre as etapas
├── etapas.py         # contratos (interfaces) de cada etapa
├── simulacao.py      # implementações fictícias, só para a demonstração
└── orquestrador.py   # encadeia as etapas
demo.py               # roda o fluxo completo com dados fictícios
```

## Demonstração

```bash
python demo.py
```

A demonstração não lê, grava nem publica nada: ela percorre o fluxo com
objetos fictícios e mostra no terminal a decisão de cada etapa.

Requisito: Python 3.10+ (sem dependências externas).

## Tecnologias do sistema real

Python, automação de navegador, processamento de mídia e reconhecimento de
fala, com agendamento pelo sistema operacional.

## Licença

**Todos os direitos reservados.** Veja [LICENSE](LICENSE). O código deste
repositório não pode ser copiado, modificado ou redistribuído sem autorização.
