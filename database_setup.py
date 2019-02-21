import sys 
from sqlalchemy import Column, ForeignKey, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()
class User(Base): 
    __tablename__='user'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(90), nullable=False)
    email = Column(String(90), nullable=False)
    picture=Column(String(350))


class Categories(Base):
    __tablename__='categories'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(45), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)



class Items(Base):
    __tablename__='items'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(45), nullable=False)
    description = Column(String(300), nullable=False)
    cat_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)



engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)