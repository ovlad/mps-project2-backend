from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class TransfusionCenter(Base):
    __tablename__ = "transfusion_center"
    id_center = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    employees = relationship("Employee", back_populates="transfusion_center")
    requests = relationship("Request", back_populates="transfusion_center")
