import typing 

from src.backend.model.user_request import AddUserRequest
from src.backend.model.abstract_response import AbstractResponse
from src.backend.model.user_response import AddUserResponse, GetUserResponse

from src.backend.data.dao.user_dao import UserDAO
from src.backend.data.entities.user import User

from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    
    def __init__(self, session: AsyncSession):
        self.session = session
        self.userDAO = UserDAO(session = session)

    async def add_user(self, user: AddUserRequest) -> AddUserResponse:

        new_user: User = User(
            USER_NAME = user.user_name,
            USER_WALLET_ADDRESS = user.user_wallet_address
        )
        new_user_dict = new_user.__dict__
        new_user_dict.pop("_sa_instance_state", None)
        await self.userDAO.add(new_user_dict)
        await self.session.commit()

        return AddUserResponse(
            USER_ID = new_user.id,
            USER_NAME = new_user.USER_NAME,
            USER_WALLET_ADDRESS = new_user.USER_WALLET_ADDRESS,
            CREATED_AT = new_user.created_at
        )
    
    async def get_user_by_id(self, user_id: int) -> GetUserResponse:

        try:
            user: User = (await self.userDAO.get_by_params(id=user_id))[0]
        except IndexError:
            # вот тут возвращать AbstractResponse
            raise ValueError(f"User with id {user_id} not found")
        
        return GetUserResponse(
            USER_ID=user.id,
            USER_NAME=user.USER_NAME,
            USER_WALLET_ADDRESS=user.USER_WALLET_ADDRESS,
            CREATED_AT=user.created_at
        )
    
    async def get_users(self, session: AsyncSession) -> typing.List[GetUserResponse]:
        
        users: typing.List[User] = await self.userDAO.get_all()

        return [GetUserResponse(
            USER_ID = user.id,
            USER_NAME = user.USER_NAME,
            USER_WALLET_ADDRESS = user.USER_WALLET_ADDRESS,
            CREATED_AT = user.created_at
        ) for user in users]
    
    async def delete_user(self, user_id: int, session: AsyncSession) -> AbstractResponse:
        await self.userDAO.delete_by_id(id = user_id)
        self.session.commit()
        return AbstractResponse()
    
    #тут проёб
    async def update_user(self, user_id: int, session: AsyncSession, request: AddUserRequest) -> AbstractResponse:

        user = await self.userDAO.get_by_id(user_id)
        user.USER_NAME = request.user_name
        user.USER_WALLET_ADDRESS = request.user_wallet_address
        await self.session.commit()

        return AbstractResponse()