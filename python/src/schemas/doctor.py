from server import ma


class DoctorSchema(ma.ModelSchema):
    class Meta:
        model = Doctor
