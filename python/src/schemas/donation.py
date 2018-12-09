from server import ma


class DonationSchema(ma.ModelSchema):
    class Meta:
        model = Donation
