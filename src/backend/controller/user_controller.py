import typing

from src.backend.controller.routes import Routes

from src.backend.service import get_user_service
from src.backend.service.user_service import UserService

from src.backend.model.user_request import AddUserRequest
from src.backend.model.abstract_response import AbstractResponse
from src.backend.model.user_response import AddUserResponse, GetUserResponse

from src.backend.data import get_session

from fastapi_utils.cbv import cbv
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
    

router = APIRouter(prefix = Routes.USER_CONTROLLER_PATH)


@cbv(router)
class UserController:
    
    #сессия лишняя - убарть
    def __init__(self, service = Depends(get_user_service)):
        self.service: UserService = service
        
    @router.post(path = "/add-user", response_model = typing.Union[AddUserResponse, AbstractResponse])
    async def add_user(self, request_body: AddUserRequest) -> typing.Union[AddUserResponse, AbstractResponse]:
        return await self.service.add_user(user = request_body)
    
    @router.get(path = "/get-user/{user_id}", response_model = typing.Union[GetUserResponse, AbstractResponse])
    async def get_user_by_id(self, user_id: int) -> typing.Union[GetUserResponse, AbstractResponse]:
        return await self.service.get_user_by_id(user_id = user_id)
    
    @router.get(path = "/get-users", response_model = typing.Union[typing.List[GetUserResponse], AbstractResponse])
    async def get_users(self) -> typing.Union[typing.List[GetUserResponse], AbstractResponse]:
        return await self.service.get_users()
    
    @router.delete(path = "/delete-user/{user_id}", response_model = AbstractResponse)
    async def delete_user_by_id(self, user_id: int) -> AbstractResponse:
        return await self.service.delete_user(user_id = user_id)
    
    @router.patch(path = "/update-user/{user_id}", response_model = AbstractResponse)
    async def update_user_by_id(self, user_id: int, request: AddUserRequest) -> AbstractResponse:
        return await self.service.update_user(user_id = user_id, request = request)
    
    


