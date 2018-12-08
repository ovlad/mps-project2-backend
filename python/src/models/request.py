from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum
from enums import RequestStatusEnum, DonorRhEnum
from sqlalchemy.orm import relationship
from database import Base


class Request(Base):
    __tablename__ = "request"
    id_request = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    status = Column(Enum(RequestStatusEnum))
    blood_type = Column(String(5), nullable=False)
    Rh = Column(Enum(DonorRhEnum), nullable=False)
    receiving_person = Column(String(60))
    quantity = Column(Float)
    id_doctor = Column(Integer, ForeignKey("doctor.id_doctor", ondelete="CASCADE"))
    id_center = Column(Integer, ForeignKey("transfusion_center.id_center", ondelete="CASCADE"))
    transfusion_center = relationship("TransfusionCenter", back_populates="requests")
    donations = relationship("Donation", back_populates="request")
    doctor = relationship("Doctor", back_populates="requests")
