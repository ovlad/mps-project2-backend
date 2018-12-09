from server import db
from enums import RequestStatusEnum, DonorRhEnum


class Employee(db.Model):
    __tablename__ = "employee"
    id_employee = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    mail = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    id_center = db.Column(db.Integer, db.ForeignKey("transfusion_center.id_center", ondelete="CASCADE"), nullable=False)
    transfusion_center = db.relationship("TransfusionCenter", back_populates="employees")


class Donor(db.Model):
    __tablename__ = "donor"
    id_donor = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    mail = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    blood_type = db.Column(db.String(5), nullable=False)
    Rh = db.Column(db.Enum(DonorRhEnum), nullable=False)
    donations = db.relationship("Donation", back_populates="donor")


class Hospital(db.Model):
    __tablename__ = "hospital"
    id_hospital = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    doctors = db.relationship("Doctor", back_populates="hospital")


class Request(db.Model):
    __tablename__ = "request"
    id_request = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    status = db.Column(db.Enum(RequestStatusEnum))
    blood_type = db.Column(db.String(5), nullable=False)
    Rh = db.Column(db.Enum(DonorRhEnum), nullable=False)
    receiving_person = db.Column(db.String(60))
    quantity = db.Column(db.Float)
    id_doctor = db.Column(db.Integer, db.ForeignKey("doctor.id_doctor", ondelete="CASCADE"))
    id_center = db.Column(db.Integer, db.ForeignKey("transfusion_center.id_center", ondelete="CASCADE"))
    transfusion_center = db.relationship("TransfusionCenter", back_populates="requests")
    donations = db.relationship("Donation", back_populates="request")
    doctor = db.relationship("Doctor", back_populates="requests")	


class TransfusionCenter(db.Model):
    __tablename__ = "transfusion_center"
    id_center = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    employees = db.relationship("Employee", back_populates="transfusion_center")
    requests = db.relationship("Request", back_populates="transfusion_center")


class Doctor(db.Model):
    __tablename__ = "doctor"
    id_doctor = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    mail = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    id_hospital = db.Column(db.Integer, db.ForeignKey("hospital.id_hospital", ondelete="CASCADE"), nullable=False)
    hospital = db.relationship("Hospital", back_populates="doctors")
    requests = db.relationship("Request", back_populates="doctor")


class Donation(db.Model):
    __tablename__ = "donation"
    id_donation = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    bloodTest = db.Column(db.BLOB)
    db.Date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Float)
    id_donor = db.Column(db.Integer, db.ForeignKey("donor.id_donor", ondelete="CASCADE"), nullable=False)
    id_request = db.Column(db.Integer, db.ForeignKey("request.id_request", ondelete="CASCADE"), nullable=False)
    donor = db.relationship("Donor", back_populates="donations")
    request = db.relationship("Request", back_populates="donations")
	
	
if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print "Creating database tables..."
    db.create_all()
    print "Done!"
