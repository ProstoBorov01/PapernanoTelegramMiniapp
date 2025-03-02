from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, DateTime


class AbstractEntity(DeclarativeBase):
    __abstract__ = True

    id = Column(Integer, primary_key = True, autoincrement = True)
    created_at = Column(DateTime, default = datetime.utcnow)
