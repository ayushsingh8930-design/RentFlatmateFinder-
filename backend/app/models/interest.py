from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Interest(Base):
    __tablename__ = "interests"

    id = Column(Integer, primary_key=True, index=True)

    tenant_id = Column(Integer, ForeignKey("tenant_profiles.id"))
    property_id = Column(Integer, ForeignKey("properties.id"))

    status = Column(String, default="Pending")

    tenant = relationship("TenantProfile")
    property = relationship("Property")