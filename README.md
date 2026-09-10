# 🛡️ Feedback Sentinel API

Microserviço desenvolvido em **Python** com **FastAPI** e a **API do Google Gemini** (`gemini-3.6-flash`) para análise automatizada de experiência do cliente (NPS/Feedbacks).

## 🚀 Funcionalidades
- **Análise de Sentimento**: Classifica feedbacks em Positivo, Neutro ou Negativo.
- **Extração de Pontos-Chave**: Resume os principais problemas ou elogios relatados pelo cliente.
- **Ação Recomendada**: Sugere medidas corretivas/preventivas automaticamente.
- **Resiliência e Retry**: Mecanismo de backoff exponencial integrado contra instabilidades da API do Gemini.

## 🛠️ Tecnologias Utilizadas
- **Python 3.13**
- **FastAPI** & **Uvicorn**
- **Google GenAI SDK** (`google-genai`)
- **Pydantic**

## 💻 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/beatrizzinkoloouresdarocha/feedback-sentinel-api-2026.git](https://github.com/beatrizzinkoloouresdarocha/feedback-sentinel-api-2026.git)
   cd feedback-sentinel-api-2026