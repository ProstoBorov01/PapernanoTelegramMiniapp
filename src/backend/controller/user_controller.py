import typing

from src.backend.controller.routes import Routes
from src.backend.service.user_service import UserService

from src.backend.model.user_request import AddUserRequest
from src.backend.model.abstract_response import AbstractResponse
from src.backend.model.user_response import AddUserResponse, GetUserResponse

from src.backend.data import AsyncSession

from fastapi_utils.cbv import cbv
from fastapi import FastAPI, APIRouter, Depends

    
router = APIRouter(prefix = Routes.USER_CONTROLLER_PATH)


@cbv(router)
class UserController:

    service: UserService = Depends(UserService)
    
    @router.post(path = "/add-user")
    async def add_user(self, request_body: AddUserRequest) -> AddUserResponse:
        return await self.service.add_user(user = request_body, session = AsyncSession())
    
    @router.get(path = "/get-user/{user_id}")
    async def get_user_by_id(self, user_id: int) -> GetUserResponse:
        return await self.service.get_user_by_id(user_id = user_id, session = AsyncSession())
    
    @router.get(path = "/get-users")
    async def get_users(self) -> typing.List[GetUserResponse]:
        return await self.service.get_users(session = AsyncSession())
    
    @router.delete(path = "/delete-user/{user_id}") 
    async def delete_user_by_id(self, user_id: int) -> AbstractResponse:
        return await self.service.delete_user(user_id = user_id, session = AsyncSession())
    
    @router.patch(path = "/update-user/{user_id}")
    async def update_user_by_id(self, user_id: int) -> AbstractResponse:
        return await self.service.update_user(user_id = user_id, session = AsyncSession())
    
    
    


