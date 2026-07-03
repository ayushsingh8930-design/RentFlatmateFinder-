from pydantic import BaseModel


class InterestCreate(BaseModel):
    tenant_id: int
    property_id: int


class InterestResponse(BaseModel):
    id: int
    tenant_id: int
    property_id: int
    status: str

    class Config:
        from_attributes = True