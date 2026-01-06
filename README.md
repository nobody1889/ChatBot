# ChatBot
A Telegram bot powered by AI (Ollama) for intelligent conversations.  
Quick to deploy with Docker and customizable with different AI models.

---

## Tech Stack
- **Language:** Python
- **Bot Implementation:** Raw Telegram API via `async` HTTP requests (`httpx`)
- **AI Model:** Ollama (gemma3)
- **Containerization:** Docker & Docker Compose
- **Database:** PostgreSQL with SQLAlchemy (async)
- **Other:** Async programming with Python `asyncio`

---

## Features
- AI-powered Telegram conversations with contextual understanding
- Supports Ollama AI models (gemma3)
- Lightweight and minimal setup required
- Quick deployment using Docker
- Optional smaller/faster AI model variant for low-resource environments
- Fully asynchronous for better performance
- Persistent conversation storage using PostgreSQL

---


## Quick Start

```bash
# 1. Build & start everything
docker compose up -d --build

# 2. Pull your AI model (only once)
docker exec -it ollama ollama pull gemma3
# Optional: smaller/faster variant
# docker exec -it ollama ollama pull gemma3:4b-it-q4_K_M

# 3. Test your Telegram bot
# Open Telegram and send a message to your bot; it should respond using the AI model.
