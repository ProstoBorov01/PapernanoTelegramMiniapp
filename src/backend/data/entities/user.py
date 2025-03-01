from src.backend.data.entities.abstract_entity import AbstractEntity

class User(AbstractEntity):
    __tablename__ = ""

    USER_NAME: str
    USER_WALLET_ADDRESS: str
    ...