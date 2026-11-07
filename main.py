
from fastapi import FastAPI
from langchain_core.language_models.fake import FakeListLLM

from models import ChatRequest, ChatResponse


app = FastAPI(
    title="TP2 - Parte 2 - Questão 1 - Fake LLM",
    description="Chatbot simulado utilizando LangChain e FastAPI",
    version="1.0.0"
)

# Perguntas e respostas predefinidas
respostas = {
    "oi": "Olá! Como posso ajudar?",
    "olá": "Olá! Como posso ajudar?",
    "o que é python?": "Python é uma linguagem de programação.",
    "o que é fastapi?": "FastAPI é um framework para criar APIs com Python.",
    "o que é langchain?": "LangChain é uma biblioteca para desenvolver aplicações com modelos de linguagem.",
    "obrigado": "Por nada! Estou à disposição."
}


@app.post("/chat", response_model=ChatResponse)
def chatbot(data: ChatRequest):

    pergunta = data.message.strip().lower()

    resposta = respostas.get(
        pergunta,
        "Não tenho uma resposta cadastrada para essa pergunta."
    )

    # Simula a resposta de um modelo de linguagem
    fake_llm = FakeListLLM(responses=[resposta])

    resultado = fake_llm.invoke(pergunta)

    return {
        "message": data.message,
        "response": resultado
    }
