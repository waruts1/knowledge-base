from sqlalchemy import Column, Integer, String , Boolean , DateTime, ForeignKey

from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    password = Column(String,nullable=False)
    date_created = Column(DateTime,nullable=False)
    location = Column(String,nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)