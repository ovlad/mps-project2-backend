from sqlalchemy import Column, Integer, ForeignKey, BLOB, Date, Float
from sqlalchemy.orm import relationship
from database import Base


class Donation(Base):
    __tablename__ = "donation"
    id_donation = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    bloodTest = Column(BLOB)
    date = Column(Date, nullable=False)
    quantity = Column(Float)
    id_donor = Column(Integer, ForeignKey("donor.id_donor", ondelete="CASCADE"), nullable=False)
    id_request = Column(Integer, ForeignKey("request.id_request", ondelete="CASCADE"), nullable=False)
    donor = relationship("Donor", back_populates="donations")
    request = relationship("Request", back_populates="donations")
