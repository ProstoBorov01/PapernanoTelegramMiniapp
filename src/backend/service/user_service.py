import typing 

from src.backend.model.user_request import AddUserRequest
from src.backend.model.abstract_response import AbstractResponse
from src.backend.model.user_response import AddUserResponse, GetUserResponse


class UserService:
    
    async def add_user(self, user: AddUserRequest) -> AddUserResponse:
        return AddUserResponse()
    
    async def get_user_by_id(self, user_id: int) -> GetUserResponse:
        return GetUserResponse()
    
    async def get_users(self, user_id: int) -> typing.List[GetUserResponse]:
        return [GetUserResponse()]
    
    async def delete_user(self, user_id: int) -> AbstractResponse:
        return AbstractResponse()
    
    async def update_user(self, user_id: int) -> AbstractResponse:
        return AbstractResponse()