# War (Python)

Uma implementação simples do jogo de cartas "War" em Python, criada como projeto didático para demonstrar organização em módulos e lógica de jogo.

## Funcionalidades

- Simulação completa de partidas entre dois jogadores
- Implementação modular: `core/` (lógica do jogo) e `utils/` (constantes)
- Execução via `main.py` com saída no terminal

## Requisitos

- Python 3.8 ou superior
- (Recomendado) Virtualenv ou outro ambiente virtual

## Instalação

Clone o repositório e instale dependências:

```bash
git clone <seu-repo-url>
cd war-python
python -m venv venv
source venv/bin/activate
```

> Não há uso de dependências externas, portanto não há arquivo de `requirements.txt`.

## Uso

Execute o jogo a partir da raiz do projeto:

```bash
python main.py
```

O jogo exibirá o progresso da partida no terminal e o resultado final.

## Estrutura do projeto

- `main.py` — ponto de entrada da aplicação
- `core/` — implementação das classes `Card`, `Deck`, `Player`, `Game`
- `utils/` — constantes e utilitários auxiliares

## Contato

Criado por Antonio Marcel. Para dúvidas ou sugestões, abra uma issue no repositório.
