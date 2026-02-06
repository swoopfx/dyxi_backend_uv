from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, relationship
from config.settings import settings


class Database:
    def __init__(self):
        self.engine = create_async_engine(settings.db_url, echo=True)
        self.SessionLocal = async_sessionmaker(self.engine, expire_on_commit=False)
        self.Base = declarative_base()

    async def get_session(self):
        async with self.SessionLocal() as session:
            yield session


db = Database()
