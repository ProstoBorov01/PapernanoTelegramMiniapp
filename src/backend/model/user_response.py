from datetime import datetime

from pydantic import BaseModel
from src.backend.model.abstract_response import AbstractResponse


class AddUserResponse(BaseModel):

    USER_ID: str
    USER_NAME: str
    USER_WALLET_ADDRESS: str
    CREATED_AT: datetime


class GetUserResponse(BaseModel):

    USER_ID: int 
    USER_NAME: str
    USER_WALLET_ADDRESS: str
    CREATED_AT: datetime