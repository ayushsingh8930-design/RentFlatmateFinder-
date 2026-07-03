from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.property import Property
from app.models.interest import Interest

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/properties")
def get_properties(db: Session = Depends(get_db)):
    return db.query(Property).all()


@router.get("/activity")
def get_activity(db: Session = Depends(get_db)):
    return {
        "users": db.query(User).count(),
        "properties": db.query(Property).count(),
        "interests": db.query(Interest).count()
    }