from sqlalchemy.orm import Session

from app.models.property import Property
from app.schemas.property import PropertyCreate


def create_property(
    db: Session,
    property_data: PropertyCreate,
    owner_id: int
):
    new_property = Property(
        title=property_data.title,
        description=property_data.description,
        city=property_data.city,
        rent=property_data.rent,
        owner_id=owner_id
    )

    db.add(new_property)
    db.commit()
    db.refresh(new_property)

    return new_property

def get_all_properties(db: Session):
    return db.query(Property).all()

def get_properties_by_city(db: Session, city: str):
    return db.query(Property).filter(Property.city == city).all()