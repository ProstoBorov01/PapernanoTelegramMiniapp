from src.backend.data.dao.abstract_dao import AbstractDAO
from sqlalchemy.ext.asyncio import AsyncSession


class UserDAO(AbstractDAO):

    def __init__(self, entity, session: AsyncSession):
        super().__init__(entity, session)
      