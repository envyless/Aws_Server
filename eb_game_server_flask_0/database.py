# database.py
# This Python file uses the following encoding: utf-8
import os, sys

#########################################
#     python 2.7.3
#########################################

from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine 이후 인자는 'mysql://사용자이름:비번@호스트이름:포트번호/연결디비 이다.

engine = create_engine(
    'mysql://yym4789:ymlso1625!@lsgame-server-db-0.czcv6ar4xswy.ap-northeast-2.rds.amazonaws.com:3306/game_main_db', convert_unicode=False, echo=True)
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))

Base = declarative_base()
# conn = engine.connect()

# mapping table class TbTest
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

def init_db():
  Base.metadata.create_all(engine)