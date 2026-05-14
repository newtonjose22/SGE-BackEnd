#test.py
from src.models.models import *
from src.database.database import SessionLocal
from src.controllers.controller import *
from src.schemas.schemas import UserCreate
db = SessionLocal()


user = UserCreate(
    name = "Robert Samuel",
    email = "robetsamuel@gmail.com",
    password = "teresajose",
    cellphone = "950846301",
    role = "Teacher",
    status = False


)

id = f'fe9378f6-b513-4d57-85e4-dab10b3954b6'
users = get_user(db)
delete(db=db, user_id=id)
for u in users:
    print('_' * 30)
    print(f'ID: {u.id}')
    print(f'{u.name} ')
    print(f'{u.email} ')
    print(f'{u.cellphone} ')
    print(f'{u.status}')
    print(f'{u.role}')
    print(f'{u.password}')
    print(f'{u.created_at}')
    

    print('-=' * 20)    

