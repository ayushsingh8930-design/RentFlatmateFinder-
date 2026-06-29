from pydantic import BaseModel


class PropertyImageCreate(BaseModel):
    image_url: str
    property_id: int


class PropertyImageResponse(BaseModel):
    id: int
    image_url: str
    property_id: int

    class Config:
        from_attributes = True