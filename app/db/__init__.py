from .deps import get_db
from .session import engine

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(conn.metadata.create_all)

__all__ = [
    "get_db",
    "init_db"
]