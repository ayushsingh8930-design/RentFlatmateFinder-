from pydantic import BaseModel


class MessageCreate(BaseModel):
    interest_id: int
    sender: str
    message: str


class MessageResponse(BaseModel):
    id: int
    interest_id: int
    sender: str
    message: str

    class Config:
        from_attributes = True