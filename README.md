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
pip install -r requirements.txt
```

> Se não houver dependências externas, o `requirements.txt` pode estar vazio.

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
- `requirements.txt` — dependências do projeto

## Desenvolvimento

- Faça alterações em ramos separados e abra PRs para revisão
- Use o ambiente virtual para executar o projeto localmente

## Contribuição

Contribuições são bem-vindas. Abra uma issue para discutir mudanças maiores ou envie um pull request com descrições claras do que foi alterado.

## Licença

Projeto pessoal — ajuste a licença conforme necessário antes de publicar.

## Contato

Criado por Antonio Marcel. Para dúvidas ou sugestões, abra uma issue no repositório.
