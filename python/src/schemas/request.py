from server import ma


class RequestSchema(ma.ModelSchema):
    class Meta:
        model = Request
