from fastapi import APIRouter, Depends
from fastapi import Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.property import PropertyCreate, PropertyResponse
from app.services.property_service import ( create_property, 
                                           get_all_properties, get_properties_by_city
                                           )

router = APIRouter(
    prefix="/properties",
    tags=["Properties"]
)


@router.post("/", response_model=PropertyResponse)
def add_property(
    property_data: PropertyCreate,
    db: Session = Depends(get_db)
):
    # Temporary: owner_id fixed hai.
    # JWT se current user nikalna next step me karenge.
    return create_property(
        db,
        property_data,
        owner_id=1
    )

@router.get("/", response_model=list[PropertyResponse])
def list_properties(db: Session = Depends(get_db)):
    return get_all_properties(db)

@router.get("/search", response_model=list[PropertyResponse])
def search_property(
    city: str = Query(...),
    db: Session = Depends(get_db)
):
    return get_properties_by_city(db, city)