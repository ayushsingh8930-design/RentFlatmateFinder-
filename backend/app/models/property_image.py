from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class PropertyImage(Base):
    __tablename__ = "property_images"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=False)

    property_id = Column(Integer, ForeignKey("properties.id"))

    property = relationship("Property", back_populates="images")