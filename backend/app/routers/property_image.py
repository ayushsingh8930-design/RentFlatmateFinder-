from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.property_image import (
    PropertyImageCreate,
    PropertyImageResponse,
)
from app.services.property_image_service import add_property_image

router = APIRouter(
    prefix="/property-images",
    tags=["Property Images"]
)


@router.post("/", response_model=PropertyImageResponse)
def create_property_image(
    image: PropertyImageCreate,
    db: Session = Depends(get_db)
):
    return add_property_image(db, image)