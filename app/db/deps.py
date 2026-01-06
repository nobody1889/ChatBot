from .session import async_sessionLocal

async def get_db():
    async with async_sessionLocal() as session:
        try:
            yield session
            await session.commit()
            
        except Exception as e:
            await session.rollback()
            raise e