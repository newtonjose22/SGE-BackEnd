from sqlalchemy import Column, Integer, String, Float, Op
from database import Base
import uuid


class Aluno(Base):
    __tablename__ = 'aluno'
    id = Column(String, primary_key=True, default=lambda : str(uuid.uuid4()), unique=True, )
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    sexo = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Matricula(Base):
    __tablename__ = 'matricula'
    id = Column(String, primary_key=True, nullable=False,)