from src.backend.data.dao.abstract_dao import AbstractDAO
from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.data.entities.user import User

class UserDAO(AbstractDAO):

    def __init__(self, session: AsyncSession):
        super().__init__(User, session)
      