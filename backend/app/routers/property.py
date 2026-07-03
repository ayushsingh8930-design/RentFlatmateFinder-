from fastapi import APIRouter, Depends
from fastapi import Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.property import PropertyCreate, PropertyResponse
from app.services.property_service import ( create_property, 
                                           get_all_properties, 
                                           get_properties_by_city,
                                           mark_property_filled
                                           )
from app.services.property_service import get_owner_properties
from app.services.property_service import delete_property
from app.services.property_service import update_property
from app.services.property_service import get_property_by_id


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

@router.get("/{property_id}", response_model=PropertyResponse)
def get_property(
    property_id: int,
    db: Session = Depends(get_db)
):
    return get_property_by_id(db, property_id)


@router.get("/owner/{owner_id}", response_model=list[PropertyResponse])
def owner_properties(owner_id: int, db: Session = Depends(get_db)):
    return get_owner_properties(db, owner_id)

@router.delete("/{property_id}")
def remove_property(
    property_id: int,
    db: Session = Depends(get_db)
):
    return delete_property(db, property_id)

@router.put("/{property_id}", response_model=PropertyResponse)
def edit_property(
    property_id: int,
    property_data: PropertyCreate,
    db: Session = Depends(get_db)
):
    return update_property(db, property_id, property_data)

@router.put("/{property_id}/filled",
            response_model=PropertyResponse)
def mark_filled(
    property_id: int,
    db: Session = Depends(get_db)
):
    return mark_property_filled(db, property_id)