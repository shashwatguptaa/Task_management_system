from fastapi import APIRouter, Depends,status,Request, BackgroundTasks
from sqlalchemy.orm import Session
from src.user import controller
from src.utils.db import get_db
from src.user.dtos import UserResponseSchema, UserSchema,LoginSchema

user_router = APIRouter(prefix="/user")

@user_router.post("/register",response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED)
async def register_user(body:UserSchema,bg_tasks: BackgroundTasks,db:Session=Depends(get_db)):
    return await controller.register(body,db, bg_tasks)

@user_router.post("/login",status_code=status.HTTP_200_OK)
def login_user(body:LoginSchema,db:Session=Depends(get_db)):
    return controller.login_user(body,db)

@user_router.get("/is_auth",status_code=status.HTTP_200_OK,response_model=UserResponseSchema)
def is_authenticated(request:Request,db:Session=Depends(get_db)):
    return controller.is_authenticated(request,db)