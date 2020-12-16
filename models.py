from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    name = Column(String)