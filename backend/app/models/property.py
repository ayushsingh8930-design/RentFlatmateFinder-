from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    city = Column(String, nullable=False)
    rent = Column(Integer, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))

    is_available = Column(Boolean, default=True)