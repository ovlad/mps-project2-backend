from server import db
from enums import RequestStatusEnum, DonorRhEnum


class Employee(db.Model):
    __tablename__ = "employee"
    idEmployee = db.Column("id_employee", db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column("mail", db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    isActive = db.Column("is_active", db.Boolean, nullable=False, default=False)
    idCenter = db.Column("id_center", db.Integer, db.ForeignKey("transfusion_center.id_center", ondelete="CASCADE"), nullable=False)
    transfusionCenter = db.relationship("TransfusionCenter", back_populates="employees")

    def __init__(self, name, surname, mail, password, idCenter):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.password = password
        self.isActive = False
        self.idCenter = idCenter


class Donor(db.Model):
    __tablename__ = "donor"
    id_donor = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column("mail", db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    bloodType = db.Column("blood_type", db.String(5), nullable=False)
    rh = db.Column("Rh", db.Enum(DonorRhEnum), nullable=False)
    donations = db.relationship("Donation", back_populates="donor")

    def __init__(self, name, surname, email, password, bloodType, rh):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.bloodType = bloodType
        self.rh = rh


class Hospital(db.Model):
    __tablename__ = "hospital"
    idHospital = db.Column("id_hospital", db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    doctors = db.relationship("Doctor", back_populates="hospital")

    def __init__(self, name):
        self.name = name


class Request(db.Model):
    __tablename__ = "request"
    idRequest = db.Column("id_request", db.Integer, primary_key=True, nullable=False, autoincrement=True)
    status = db.Column(db.Enum(RequestStatusEnum))
    bloodType = db.Column("blood_type", db.String(5), nullable=False)
    rh = db.Column("Rh", db.Enum(DonorRhEnum), nullable=False)
    receivingPerson = db.Column("receiving_person", db.String(60))
    quantity = db.Column(db.Float)
    idDoctor = db.Column("id_doctor", db.Integer, db.ForeignKey("doctor.id_doctor", ondelete="CASCADE"))
    idCenter = db.Column("id_center", db.Integer, db.ForeignKey("transfusion_center.id_center", ondelete="CASCADE"))
    transfusionCenter = db.relationship("TransfusionCenter", back_populates="requests")
    donations = db.relationship("Donation", back_populates="request")
    doctor = db.relationship("Doctor", back_populates="requests")

    def __init__(self, bloodType, rh, receivingPerson, quantity, idDoctor, idCenter):
        self.status = RequestStatusEnum.Donation
        self.bloodType = bloodType
        self.rh = rh
        self.receivingPerson = receivingPerson
        self.quantity = quantity
        self.idDoctor = idDoctor
        self.idCenter = idCenter



class TransfusionCenter(db.Model):
    __tablename__ = "transfusion_center"
    idCenter = db.Column("id_center", db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    employees = db.relationship("Employee", back_populates="transfusion_center")
    requests = db.relationship("Request", back_populates="transfusion_center")

    def __init__(self, name):
        self.name = name


class Doctor(db.Model):
    __tablename__ = "doctor"
    idDoctor = db.Column("id_doctor", db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column("mail", db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    isActive = db.Column("is_active", db.Boolean, nullable=False, default=False)
    idHospital = db.Column("id_hospital", db.Integer, db.ForeignKey("hospital.id_hospital", ondelete="CASCADE"), nullable=False)
    hospital = db.relationship("Hospital", back_populates="doctors")
    requests = db.relationship("Request", back_populates="doctor")

    def __init__(self, name, surname, email, password, idHospital):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.isActive = False
        self.idHospital = idHospital

class Donation(db.Model):
    __tablename__ = "donation"
    idDonation = db.Column("id_donation", db.Integer, primary_key=True, nullable=False, autoincrement=True)
    bloodTest = db.Column(db.BLOB)
    date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Float)
    idDonor = db.Column("id_donor", db.Integer, db.ForeignKey("donor.id_donor", ondelete="CASCADE"), nullable=False)
    idRequest = db.Column("id_request", db.Integer, db.ForeignKey("request.id_request", ondelete="CASCADE"), nullable=False)
    donor = db.relationship("Donor", back_populates="donations")
    request = db.relationship("Request", back_populates="donations")

    def __init__(self, bloodTest, date, quantity, idDonor, idRequest):
        self.bloodTest = bloodTest
        self.date = date
        self.quantity = quantity
        self.idDonor = idDonor
        self.idRequest = idRequest


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print "Creating database tables..."
    db.create_all()
    print "Done!"
