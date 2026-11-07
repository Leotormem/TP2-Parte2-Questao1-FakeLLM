
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        description="Mensagem enviada pelo usuário"
    )


class ChatResponse(BaseModel):
    message: str
    response: str
