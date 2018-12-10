from server import ma
from marshmallow_enum import EnumField
from enums import RequestStatusEnum, DonorRhEnum
from models import Doctor, Donation, Donor, Employee, Hospital, Request, TransfusionCenter


class DonationSchema(ma.ModelSchema):
    class Meta:
        model = Donation


class DonorSchema(ma.ModelSchema):
    rh = EnumField(DonorRhEnum)

    class Meta:
        model = Donor


class EmployeeSchema(ma.ModelSchema):
    class Meta:
        model = Employee


class HospitalSchema(ma.ModelSchema):
    class Meta:
        model = Hospital


class RequestSchema(ma.ModelSchema):
    status = EnumField(RequestStatusEnum)
    rh = EnumField(DonorRhEnum)

    class Meta:
        model = Request


class TransfusionCenterSchema(ma.ModelSchema):
    class Meta:
        model = TransfusionCenter


class DoctorSchema(ma.ModelSchema):
    class Meta:
        model = Doctor
