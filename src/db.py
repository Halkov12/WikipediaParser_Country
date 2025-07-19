import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

class DBManager:
    def __init__(self, database_url=None):
        self.DATABASE_URL = database_url or os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/countries")
        self.engine = create_async_engine(self.DATABASE_URL, echo=False, future=True)
        self.Base = declarative_base()
        self.AsyncSessionLocal = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    async def init_db(self):
        async with self.engine.begin() as conn:
            from models import Country  # noqa: F401
            await conn.run_sync(self.Base.metadata.create_all)

db_manager = DBManager() 