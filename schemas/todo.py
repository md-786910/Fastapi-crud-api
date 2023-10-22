from sqlalchemy import String, Column,Integer

from db.connection import Base

class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer,autoincrement=True, primary_key=True, nullable=False)
    title= Column(String,nullable=False)
    description= Column(String,nullable=False)
    