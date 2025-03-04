from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete


class AbstractDAO:

    def __init__(self, entity, session: AsyncSession):
        self.entity = entity
        self.session = session

    async def get_all(self) -> list:
        sql = select(self.entity)
        data = await self.session.execute(sql)
        return list(data.scalar().all())
    
    async def get_by_params(self, **params) -> list:
        sql = select(self.entity).filter_by(**params)
        data = await self.session.execute(sql)
        return list(data.scalars().unique().all())
    

    async def add(self, data: dict):
        sql = insert(self.entity).values(**data).returning(self.entity)
        row = await self.session.execute(sql)
        return row.scalar()

    async def edit_by_id(self, id: int, **params) -> None:
        sql = update(self.entity).where(self.entity.id == id).values(**params)
        await self.session.execute(sql)

    async def delete_by_id(self, id: int):
        sql = delete(self.entity).where(self.entity.id == id)
        await self.session.execute(sql)