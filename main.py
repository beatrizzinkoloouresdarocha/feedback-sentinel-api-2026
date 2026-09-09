import json
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from google import genai
from google.genai import types
from google.genai.errors import APIError
from pydantic import BaseModel

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY não encontrada nas variáveis de ambiente.")

client = genai.Client(api_key=api_key)

app = FastAPI(
    title="Feedback Sentinel API",
    description="Microserviço para análise de sentimento e resumo de feedbacks usando IA.",
    version="1.0.0",
)


class FeedbackRequest(BaseModel):
    cliente: str
    comentario: str


class FeedbackResponse(BaseModel):
    sentimento: str
    pontos_chave: str
    acao_recomendada: str


@app.get("/health", tags=["Healthcheck"])
def health_check():
    return {"status": "ok", "service": "online"}


@app.post("/analisar-feedback", response_model=FeedbackResponse, tags=["Análise"])
def analisar_feedback(data: FeedbackRequest):
    prompt = f"""
    Você é um assistente de análise de experiência do cliente.
    Analise o seguinte comentário enviado pelo cliente {data.cliente}:
    "{data.comentario}"
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=FeedbackResponse,
            ),
        )

        # O retorno usando response_schema aceita conversão via json.loads
        resultado = json.loads(response.text)
        return resultado

    except (APIError, ValueError, json.JSONDecodeError) as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao processar análise: {e!s}"
        )