from sqlalchemy.orm import Session

from app.models.tenant_profile import TenantProfile
from app.schemas.tenant_profile import TenantProfileCreate


def create_tenant_profile(
    db: Session,
    profile: TenantProfileCreate,
    user_id: int
):
    tenant_profile = TenantProfile(
        user_id=user_id,
        preferred_location=profile.preferred_location,
        budget=profile.budget,
        move_in_date=profile.move_in_date
    )

    db.add(tenant_profile)
    db.commit()
    db.refresh(tenant_profile)

    return tenant_profile