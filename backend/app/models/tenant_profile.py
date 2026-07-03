from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class TenantProfile(Base):
    __tablename__ = "tenant_profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    preferred_location = Column(String, nullable=False)
    budget = Column(Integer, nullable=False)
    move_in_date = Column(String, nullable=False)

    user = relationship("User")