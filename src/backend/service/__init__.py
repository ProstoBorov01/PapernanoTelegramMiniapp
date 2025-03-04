from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.data import get_session
from src.backend.data import get_session

from src.backend.service.user_service import UserService

from fastapi import Depends

async def get_user_service(session: AsyncSession = Depends(get_session)) -> UserService:
    return UserService(session = session)