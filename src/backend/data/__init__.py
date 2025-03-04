from typing import AsyncGenerator

from src.backend.data.entities.user import User
from src.backend.model.config import DatabaseConfig

from sqlalchemy import Inspector
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine


#asyncpg для асинхронного подключения, без него не будет работать
database_url = f"postgresql+asyncpg://{DatabaseConfig.USERNAME}:{DatabaseConfig.PASSWORD}@{DatabaseConfig.SERVER_ADDRESS}/{DatabaseConfig.DATABASE_NAME}"
async_engine: AsyncEngine = create_async_engine(url = database_url, echo = True)

async_session = sessionmaker(bind = async_engine, class_ = AsyncSession, expire_on_commit = False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


 # вот тут в будущем все таблицы таким образом необходимо добавить(данный метод создаёт таблицы, если они не были созданы)
async def create_tables(engine: AsyncEngine) -> None:
    async with engine.begin() as connection:
        exists = await connection.run_sync(
            lambda sync_conn: Inspector.from_engine(sync_conn).has_table(User.__tablename__)
        )
        if not exists:
            await connection.run_sync(User.metadata.create_all)