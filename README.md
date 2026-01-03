# ChatBot
A Telegram bot powered by AI (Ollama) for intelligent conversations.

## Quick Start

```bash
# 1. Build & start everything
docker compose up -d --build

# 2. Pull your model (do this only once)
docker exec -it ollama ollama pull gemma3
# Optional smaller/faster variant:
# docker exec -it ollama ollama pull gemma3:4b-it-q4_K_M

# 3. Check your telegram bot
