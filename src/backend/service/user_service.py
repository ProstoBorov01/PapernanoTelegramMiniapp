import typing 

from src.backend.model.user_request import AddUserRequest
from src.backend.model.abstract_response import AbstractResponse
from src.backend.model.user_response import AddUserResponse, GetUserResponse

from sqlalchemy.orm import Session


class UserService:
    
    async def add_user(self, user: AddUserRequest, session: Session) -> AddUserResponse:
        return AddUserResponse()
    
    async def get_user_by_id(self, user_id: int, session: Session) -> GetUserResponse:
        return GetUserResponse()
    
    async def get_users(self, user_id: int, session: Session) -> typing.List[GetUserResponse]:
        return [GetUserResponse()]
    
    async def delete_user(self, user_id: int, session: Session) -> AbstractResponse:
        return AbstractResponse()
    
    async def update_user(self, user_id: int, session: Session) -> AbstractResponse:
        return AbstractResponse()