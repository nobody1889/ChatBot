from .session import async_sessionLocal

async def get_db():
    async with async_sessionLocal() as session:
        yield session