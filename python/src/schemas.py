from server import ma
from marshmallow_enum import EnumField
from marshmallow import fields
from enums import RequestStatusEnum, DonorRhEnum
from models import Doctor, Donation, Donor, Employee, Hospital, Request, TransfusionCenter


class DonorSchema(ma.ModelSchema):
    rh = EnumField(DonorRhEnum)

    class Meta:
        model = Donor


class DonationSchema(ma.ModelSchema):
    donor = ma.Nested(DonorSchema)
    date = fields.DateTime(format="%d/%m/%Y")
    request = ma.Nested('RequestSchema', only=("receivingPerson", "status"))

    class Meta:
        model = Donation


class EmployeeSchema(ma.ModelSchema):
    class Meta:
        model = Employee


class HospitalSchema(ma.ModelSchema):
    class Meta:
        model = Hospital


class TransfusionCenterSchema(ma.ModelSchema):
    class Meta:
        model = TransfusionCenter


class DoctorSchema(ma.ModelSchema):
    class Meta:
        model = Doctor


class RequestSchema(ma.ModelSchema):
    status = EnumField(RequestStatusEnum)
    rh = EnumField(DonorRhEnum)
    donations = ma.Nested(DonationSchema, many=True)
    doctor = ma.Nested(DoctorSchema)
    transfusionCenter = ma.Nested(TransfusionCenterSchema)

    class Meta:
        model = Request
