from pydantic import BaseModel
from src.backend.model.abstract_response import AbstractResponse


class AddUserResponse(BaseModel, AbstractResponse):

    USER_NAME: str
    USER_WALLET_ADDRESS: str


class GetUserResponse(BaseModel, AbstractResponse):

    USER_ID: int 
    USER_NAME: str
    USER_WALLET_ADDRESS: str