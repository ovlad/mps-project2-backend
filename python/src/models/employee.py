from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = "employee"
    id_employee = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    mail = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    is_active = Column(TINYINT(1), nullable=False, default=0)
    id_center = Column(Integer, ForeignKey("transfusion_center.id_center"), nullable=False)
    transfusion_center = relationship("TransfusionCenter", back_populates="employees", ondelete="CASCADE")
