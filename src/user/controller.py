from src.user.dtos import UserSchema
from SQLAlchemy.orm import Session

def register(body:UserSchema,db:Session):
    print(body)
    return {"message":"User registered successfully"}