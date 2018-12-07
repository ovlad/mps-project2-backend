from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Doctor(Base):
    __tablename__ = "doctor"
    id_doctor = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    mail = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    is_active = Column(TINYINT(1), nullable=False, default=0)
    id_hospital = Column(Integer, ForeignKey("hospital.id_hospital"), nullable=False, ondelete="CASCADE")
    hospital = relationship("Hospital", back_populates="doctors")
    requests = relationship("Request", back_populates="doctor")
