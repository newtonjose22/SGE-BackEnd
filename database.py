from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

URL = 'sqllite:///./main_db.db'
engine = create_engine(URL, connect_args={'check_same_threads' : False})

SessionLocal = sessionmaker(bind=engine, )
Base = declarative_base()

def getdb():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()