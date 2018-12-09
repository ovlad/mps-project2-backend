from server import ma


class DonorSchema(ma.ModelSchema):
    class Meta:
        model = Donor
