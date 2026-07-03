from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.compatibility import (
    CompatibilityCreate,
    CompatibilityResponse,
)
from app.services.compatibility_service import calculate_score

router = APIRouter(
    prefix="/compatibility",
    tags=["Compatibility"]
)


@router.post("/", response_model=CompatibilityResponse)
def compatibility(
    data: CompatibilityCreate,
    db: Session = Depends(get_db)
):
    return calculate_score(
        db,
        data.tenant_id,
        data.property_id
    )