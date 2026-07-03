from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.interest import (
    InterestCreate,
    InterestResponse
)
from app.services.interest_service import (
    send_interest,
    accept_interest,
    decline_interest
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

@router.put("/{interest_id}/accept",
            response_model=InterestResponse)
def accept(
    interest_id: int,
    db: Session = Depends(get_db)
):
    return accept_interest(db, interest_id)

@router.put("/{interest_id}/decline",
            response_model=InterestResponse)
def decline(
    interest_id: int,
    db: Session = Depends(get_db)
):
    return decline_interest(db, interest_id)