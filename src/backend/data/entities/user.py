from sqlalchemy import Column, String

from src.backend.data.entities.abstract_entity import AbstractEntity

class User(AbstractEntity):
    __tablename__ = "Users"

    user_name: str = Column(String, nullable = False)
    user_wallet_address: str = Column(String, nullable = False)
    ...