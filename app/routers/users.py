from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, auth_utils
from ..database import get_db

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get("/")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user not found')
    
    return user


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # check the email for if it exists
    existing_user = db.query(models.Users).filter(models.Users.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'{user.email} already exists')
    
    # hash the password then push the data to db
    hashed_password = auth_utils.hash_password(user.password)
    user.password = hashed_password
    new_user = models.Users(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user