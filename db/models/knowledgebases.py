from sqlalchemy import Column, Integer, String , Boolean , DateTime, ForeignKey

from sqlalchemy.orm import relationship

from db.base_class import Base


class KnowledgeBase(Base):
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String, nullable=False)
    category_id = Column(Integer, foreign_key = True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    description = Column(String, nullable=False)
    date_created = Column(DateTime, nullable=False)
    is_active = Column(Boolean)
    user = relationship("User",back_populates="user")
    category = relationship("Category",back_populates="category")
    