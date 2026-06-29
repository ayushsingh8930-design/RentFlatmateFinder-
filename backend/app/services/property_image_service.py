from sqlalchemy.orm import Session
from app.models.property_image import PropertyImage
from app.schemas.property_image import PropertyImageCreate


def add_property_image(db: Session, image: PropertyImageCreate):
    db_image = PropertyImage(
        image_url=image.image_url,
        property_id=image.property_id
    )

    db.add(db_image)
    db.commit()
    db.refresh(db_image)

    return db_image