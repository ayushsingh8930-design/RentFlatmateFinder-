from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.tenant_profile import (
    TenantProfileCreate,
    TenantProfileResponse,
)
from app.services.tenant_profile_service import create_tenant_profile

router = APIRouter(
    prefix="/tenant-profile",
    tags=["Tenant Profile"]
)


@router.post("/", response_model=TenantProfileResponse)
def add_profile(
    profile: TenantProfileCreate,
    db: Session = Depends(get_db)
):
    # Temporary user_id
    return create_tenant_profile(
        db,
        profile,
        user_id=1
    )