from sqlalchemy.orm import Session

from app.models.compatibility import Compatibility
from app.models.tenant_profile import TenantProfile
from app.models.property import Property
from app.services.ai_service import rule_based_score
from app.services.ai_service import gemini_score

def calculate_score(db: Session, tenant_id: int, property_id: int):

    tenant = db.query(TenantProfile).filter(
        TenantProfile.id == tenant_id
    ).first()

    property = db.query(Property).filter(
        Property.id == property_id
    ).first()
    print("tenant_id =", tenant_id)
    print("property_id =", property_id)
    print("tenant =", tenant)
    print("property =", property)





    result = gemini_score(tenant, property)

    score = result["score"]
    explanation = result["explanation"]

    compatibility = Compatibility(
    tenant_id=tenant_id,
    property_id=property_id,
    score=score,
    explanation=explanation
)
    

    db.add(compatibility)
    db.commit()
    db.refresh(compatibility)

    return compatibility