from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Hospital(Base):
    __tablename__ = "hospital"
    id_hospital = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    doctors = relationship("Doctor", back_populates="hospital")
