from sqlalchemy.orm import Session

from app.models.interest import Interest
from app.schemas.interest import InterestCreate


def send_interest(
    db: Session,
    interest: InterestCreate
):
    db_interest = Interest(
        tenant_id=interest.tenant_id,
        property_id=interest.property_id
    )

    db.add(db_interest)
    db.commit()
    db.refresh(db_interest)

    return db_interest

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.interest import (
    InterestCreate,
    InterestResponse
)
from app.services.interest_service import send_interest

router = APIRouter(
    prefix="/interest",
    tags=["Interest"]
)


@router.post("/", response_model=InterestResponse)
def create_interest(
    interest: InterestCreate,
    db: Session = Depends(get_db)
):
    return send_interest(db, interest)

def accept_interest(db: Session, interest_id: int):
    interest = db.query(Interest).filter(
        Interest.id == interest_id
    ).first()

    if not interest:
        return {"message": "Interest not found"}

    interest.status = "Accepted"

    db.commit()
    db.refresh(interest)

    return interest


def decline_interest(db: Session, interest_id: int):
    interest = db.query(Interest).filter(
        Interest.id == interest_id
    ).first()

    if not interest:
        return {"message": "Interest not found"}

    interest.status = "Declined"

    db.commit()
    db.refresh(interest)

    return interest