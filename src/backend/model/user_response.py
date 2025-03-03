from datetime import datetime

from pydantic import BaseModel
from src.backend.model.abstract_response import AbstractResponse


class AddUserResponse(BaseModel):

    user_id: str
    user_name: str
    user_wallet_address: str
    created_at: datetime


class GetUserResponse(BaseModel):

    user_id: int 
    user_name: str
    user_wallet_address: str
    created_at: datetime