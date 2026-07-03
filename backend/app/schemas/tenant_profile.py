from pydantic import BaseModel


class TenantProfileCreate(BaseModel):
    preferred_location: str
    budget: int
    move_in_date: str


class TenantProfileResponse(BaseModel):
    id: int
    user_id: int
    preferred_location: str
    budget: int
    move_in_date: str

    class Config:
        from_attributes = True