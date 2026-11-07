# TP2 — Parte 2, Questão 1: Chatbot com Fake LLM

## Descrição

Neste projeto desenvolvi um chatbot simples utilizando FastAPI e LangChain. A aplicação recebe perguntas em JSON e retorna respostas simuladas através do FakeListLLM.

O objetivo é demonstrar como integrar o LangChain com uma API, sem precisar utilizar um modelo de linguagem real.

## Tecnologias utilizadas

- Python
- FastAPI
- LangChain Core
- Pydantic
- Uvicorn

## Estrutura do projeto

```text
parte2_questao1_fake_llm/
├── main.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Funcionamento

O usuário envia uma mensagem para a rota POST /chat. O FastAPI recebe e valida o JSON utilizando Pydantic.

A aplicação consulta um dicionário de perguntas e respostas previamente cadastradas e utiliza o FakeListLLM para simular a resposta do chatbot.

Quando uma pergunta não está cadastrada, o sistema retorna uma mensagem padrão.

## Arquitetura

```text
Usuário
  |
  v
FastAPI - POST /chat
  |
  v
Validação Pydantic
  |
  v
Consulta às respostas cadastradas
  |
  v
LangChain - FakeListLLM
  |
  v
Resposta JSON
```

## Instalação

Crie um ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente no Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

## Execução

Inicie o servidor:

```powershell
python -m uvicorn main:app --reload
```

Acesse a documentação Swagger:

http://127.0.0.1:8000/docs

## Exemplo de utilização

Requisição POST /chat:

```json
{
  "message": "o que é python?"
}
```

Resposta:

```json
{
  "message": "o que é python?",
  "response": "Python é uma linguagem de programação."
}
```

## Importância do Fake LLM

O Fake LLM permite testar o funcionamento de uma aplicação sem realizar chamadas a serviços externos ou carregar modelos de linguagem grandes.

Isso facilita o desenvolvimento inicial, a validação das rotas HTTP e a realização de testes rápidos.

## Limitações

O chatbot utiliza respostas previamente cadastradas. Portanto, não gera textos novos e não compreende perguntas que não estejam previstas.

O FakeListLLM apenas simula a interface de um modelo de linguagem. Ele não substitui um LLM real.

## Autor

Leonardo Luiz Tormem