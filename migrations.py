from src.database.database import Base, engine
from src.models.models import *

Base.metadata.create_all(bind=engine)
print('Feito')