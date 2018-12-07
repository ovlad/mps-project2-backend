from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from enums import DonorRhEnum


class Donor(Base):
    __tablename__ = "donor"
    id_donor = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    mail = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    blood_type = Column(String(5), nullable=False)
    Rh = Column(Enum(DonorRhEnum), nullable=False)
    donations = relationship("Donation", back_populates="donor")
