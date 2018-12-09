from server import ma


class EmployeeSchema(ma.ModelSchema):
    class Meta:
        model = Employee
