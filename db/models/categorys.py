from sqlalchemy import Column, Integer, String , Boolean , DateTime, ForeignKey

from sqlalchemy.orm import relationship

from db.base_class import Base


class Category(Base):
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, foreign_key=True,nullable=False)
    description = Column(String, nullable=False)
    date_created = Column(DateTime, nullable=False)
    is_active = Column(Boolean())
    knowledgebase = relationship("KnowledgeBase",back_populates="knowledgebase")
    user = relationship("User",back_populates="user")