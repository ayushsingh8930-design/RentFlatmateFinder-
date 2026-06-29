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

def get_owner_properties(db, owner_id):
    return db.query(Property).filter(Property.owner_id == owner_id).all()

def delete_property(db: Session, property_id: int):
    property = db.query(Property).filter(Property.id == property_id).first()

    if not property:
        return {"message": "Property not found"}

    db.delete(property)
    db.commit()

    return {"message": "Property deleted successfully"}

def update_property(db: Session, property_id: int, property_data: PropertyCreate):
    property = db.query(Property).filter(Property.id == property_id).first()

    if not property:
        return {"message": "Property not found"}

    property.title = property_data.title
    property.description = property_data.description
    property.city = property_data.city
    property.rent = property_data.rent

    db.commit()
    db.refresh(property)

    return property