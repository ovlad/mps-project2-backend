from server import ma


class HospitalSchema(ma.ModelSchema):
    class Meta:
        model = Hospital
