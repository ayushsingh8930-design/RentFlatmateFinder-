from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship  
from app.database import Base


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    city = Column(String, nullable=False)
    rent = Column(Integer, nullable=False)
    available_from = Column(String, nullable=False)

    room_type = Column(String, nullable=False)

    furnishing_status = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="properties")
    is_available = Column(Boolean, default=True)

    images = relationship("PropertyImage", back_populates="property")

    