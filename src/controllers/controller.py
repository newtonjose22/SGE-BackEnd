from src.models.models import *
from src.schemas import  schemas
from sqlalchemy.orm import Session

def create_user(db: Session, user:schemas.UserCreate):
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user(db: Session):
    users = db.query(User).all()

    return users

def getuser_by_ID(db: Session, user_id:str):
    user = db.query(User).filter(User.id == user_id).all()
    return user

def getuser_status(db:Session, status: bool):
    user_status = db.query(User).filter(User.status == status).all()

    return user_status

def delete(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        return None  # utilizador não existe
    db.delete(user)
    db.commit()  # <- faltava isto
    return {"message": "Utilizador eliminado com sucesso"}