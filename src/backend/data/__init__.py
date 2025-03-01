from src.backend.model.config import DatabaseConfig

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


database_url = f"postgresql://{DatabaseConfig.DATABASE_NAME}:{DatabaseConfig.PASSWORD}@{DatabaseConfig.SERVER_ADDRESS}/{DatabaseConfig.DATABASE_NAME}"
async_engine = create_async_engine(url = database_url, echo = True)

AsyncSession = sessionmaker(bind = async_engine, class_ = AsyncSession, expire_on_commit = False)
