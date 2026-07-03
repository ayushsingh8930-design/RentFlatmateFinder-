from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    interest_id = Column(Integer, ForeignKey("interests.id"))

    sender = Column(String)

    message = Column(String)