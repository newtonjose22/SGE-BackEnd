from models.models import *
from database.database import SessionLocal

db = SessionLocal()


curso1 = Course(nome="Comercio")
curso2 = Course(nome="Informatica")
curso3 = Course(nome="Gestão De Recurso Humanos")
curso4 = Course(nome="Contablidade")
curso5 = Course(nome="Gestão empresarial")
curso6 = Course(nome="Informatcica De Gestão")
curso7 = Course(nome="Finanças")

db.add_all(curso1, curso2, curso3,curso4,curso5, curso6, curso7)
db.commit()
