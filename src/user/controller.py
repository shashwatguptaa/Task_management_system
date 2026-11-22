from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from fastapi import HTTPException,status, Request
from pwdlib import PasswordHash 
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from src.utils.settings import settings
from src.utils.mail import send_email

password_hash = PasswordHash.recommended()
def get_password_hash(password:str):
    return password_hash.hash(password)

async def register(body:UserSchema,db:Session):
    is_user = db.query(UserModel).filter(UserModel.username==body.username).first()
    if is_user:
        raise HTTPException(status_code=400,detail="User already exists")
    is_email = db.query(UserModel).filter(UserModel.email==body.email).first()
    if is_email:
        raise HTTPException(status_code=400,detail="Email already exists")
    hash_password = get_password_hash(body.password)
    new_user = UserModel(name=body.name,username=body.username,email=body.email,password=hash_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    await send_email([new_user.email])
    return new_user

def login_user(body:LoginSchema,db:Session):
    user = db.query(UserModel).filter(UserModel.username==body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    if not password_hash.verify(body.password,user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password")
    exp_time = datetime.now()+timedelta(minutes=settings.EXP_TIME)
    token = jwt.encode({"_id": user.id,"exp": exp_time.timestamp()}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return {"token" : token}

def is_authenticated(request:Request, db:Session):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token not found")    
        token = token.split(" ")[1] 
        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user_id = data["_id"]
        user = db.query(UserModel).filter(UserModel.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")
