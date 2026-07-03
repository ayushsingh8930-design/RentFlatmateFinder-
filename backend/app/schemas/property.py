from pydantic import BaseModel


class PropertyCreate(BaseModel):
    title: str
    description: str
    city: str
    rent: int

    available_from: str
    room_type: str
    furnishing_status: str


class PropertyResponse(BaseModel):
    id: int
    title: str
    description: str
    city: str
    rent: int

    available_from: str
    room_type: str
    furnishing_status: str

    owner_id: int
    is_available: bool

    class Config:
        from_attributes = True