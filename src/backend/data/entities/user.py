from sqlalchemy import Column, String

from src.backend.data.entities.abstract_entity import AbstractEntity

class User(AbstractEntity):
    __tablename__ = "Users"

    USER_NAME: str = Column(String, nullable = False)
    USER_WALLET_ADDRESS: str = Column(String, nullable = False)
    ...