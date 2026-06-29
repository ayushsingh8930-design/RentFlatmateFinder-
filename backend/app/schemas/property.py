from pydantic import BaseModel


class PropertyCreate(BaseModel):
    title: str
    description: str
    city: str
    rent: int


class PropertyResponse(BaseModel):
    id: int
    title: str
    description: str
    city: str
    rent: int
    owner_id: int
    is_available: bool

    class Config:
        from_attributes = True