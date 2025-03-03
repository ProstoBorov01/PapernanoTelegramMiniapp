import typing 

from src.backend.model.user_request import AddUserRequest
from src.backend.model.abstract_response import AbstractResponse
from src.backend.model.user_response import AddUserResponse, GetUserResponse

from src.backend.data.entities.user import User
from src.backend.data.dao.user_dao import UserDAO

from sqlalchemy.ext.asyncio import AsyncSession

from http import HTTPStatus


class UserService:
    
    def __init__(self, session: AsyncSession):
        self.session = session
        self.userDAO = UserDAO(session = session)

    async def add_user(self, user: AddUserRequest) -> typing.Union[AddUserResponse, AbstractResponse]:
        try:
            new_user: User = User(
                user_name = user.user_name,
                user_wallet_address = user.user_wallet_address
            )
            new_user_dict = new_user.__dict__
            new_user_dict.pop("_sa_instance_state", None)
            await self.userDAO.add(new_user_dict)
            await self.session.commit()
            await self.session.refresh(new_user)
            return AddUserResponse(
                user_id = new_user.id,
                user_name = new_user.user_name,
                user_wallet_address = new_user.user_wallet_address,
                created_at = new_user.created_at
            )
        except Exception as ex:
            self.session.rollback()
            return AbstractResponse(
                message = f"Error: {ex}",
                status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            )
        
    async def get_user_by_id(self, user_id: int) -> typing.Union[GetUserResponse, AbstractResponse]:
        try:
            user: User = (await self.userDAO.get_by_params(id=user_id))[0]
        except IndexError:
            return AbstractResponse(
                message = f"User with id {user_id} not found",
                status_code = HTTPStatus.BAD_REQUEST
            )
        return GetUserResponse(
            user_id = user.id,
            user_name = user.user_name,
            user_wallet_address = user.user_wallet_address,
            created_at = user.created_at
        )
    
    async def get_users(self) -> typing.Union[typing.List[GetUserResponse], AbstractResponse]:
        users: typing.List[User] = await self.userDAO.get_all()
        return (
            [
                GetUserResponse(
                    user_id = user.id,
                    user_name = user.user_name,
                    user_wallet_address = user.user_wallet_address,
                    created_at = user.created_at
                ) for user in users
            ]
        )
    
    async def delete_user(self, user_id: int) -> AbstractResponse:
        try:
            await self.userDAO.delete_by_id(id=user_id)
            await self.session.commit()
            return AbstractResponse(
                message="User deleted successfully"
            )
        except Exception as ex:
            await self.session.rollback()
            return AbstractResponse(
                message=f"Error: {ex}",
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR
            )

    async def update_user(self, user_id: int, request: AddUserRequest) -> AbstractResponse:
        try:
            user: User = await self.userDAO.get_by_id(user_id)
            if not user:
                return AbstractResponse(
                    message = f"User with id {user_id} not found",
                    status_code = HTTPStatus.BAD_REQUEST
                )
            
            user.user_name = request.user_name
            user.user_wallet_address = request.user_wallet_address
            await self.session.commit()
            return AbstractResponse(
                message = "User updated successfully"
            )
        except Exception as ex:
            await self.session.rollback()
            return AbstractResponse(
                message = f"Error: {ex}",
                status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            )