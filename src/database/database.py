from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

URL = 'sqlite:///./main_db.db'
engine = create_engine(URL, connect_args={'check_same_thread' : False})

SessionLocal = sessionmaker(bind=engine, )
Base = declarative_base()

def getdb():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()