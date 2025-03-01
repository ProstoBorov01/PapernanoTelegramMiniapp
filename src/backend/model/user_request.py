from pydantic import BaseModel


class AddUserRequest(BaseModel):

    user_name: str
    user_wallet_address: str


