from pydantic import BaseModel


class CompatibilityCreate(BaseModel):
    tenant_id: int
    property_id: int


class CompatibilityResponse(BaseModel):
    id: int
    tenant_id: int
    property_id: int
    score: int
    explanation: str

    class Config:
        from_attributes = True