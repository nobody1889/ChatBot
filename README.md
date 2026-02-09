# 📬 ChatBot — AI-Powered Telegram Bot

A Telegram bot powered by **AI (Ollama)** for smart conversations.  
Lightweight, async, Docker-ready, and easily customizable with different AI models.

---

## 🚀 Features

- 💬 Intelligent replies using Ollama AI models
- 🧠 Context-aware conversation handling
- ⚡ Fully asynchronous (FastAPI + async httpx + asyncio)
- 🐳 Easy deployment with Docker & Docker Compose
- 🗃 Persistent message storage via PostgreSQL + SQLAlchemy (async)
- 🧠 Support for different AI models (including faster/lighter variants)

---

## 🧱 Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python (FastAPI) |
| Telegram Bot | Telegram Bot API (async HTTP via httpx) |
| AI Backend | Ollama |
| Database | PostgreSQL |
| ORM | SQLAlchemy (async) |
| Deployment | Docker & Docker Compose |

---

## 📦 Prerequisites

Before starting, make sure you have:

- Docker & Docker Compose installed
- A Telegram bot token (from @BotFather)
- Enough resources to run the Ollama AI container

---

## ⚙️ Configuration

Rename `.env.example` ➝ `.env` and set the following:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
DATABASE_URL=postgresql+asyncpg://user:pass@postgres/dbname
OLLAMA_URL=http://ollama:11434
