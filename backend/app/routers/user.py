from fastapi import HTTPException
from app.schemas.user import UserLogin, Token
from app.services.user_service import login_user

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserSignup, UserResponse
from app.services.user_service import create_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/signup", response_model=UserResponse)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    result = login_user(
        db,
        user.email,
        user.password
    )

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return result