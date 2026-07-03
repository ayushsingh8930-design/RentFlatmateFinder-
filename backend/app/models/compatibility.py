from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Compatibility(Base):
    __tablename__ = "compatibility"

    id = Column(Integer, primary_key=True, index=True)

    tenant_id = Column(Integer, ForeignKey("tenant_profiles.id"))
    property_id = Column(Integer, ForeignKey("properties.id"))

    score = Column(Integer)
    explanation = Column(String)

    tenant = relationship("TenantProfile")
    property = relationship("Property")