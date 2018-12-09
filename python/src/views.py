from server import app, db
from flask import request, jsonify
from models import Doctor, Donation, Donor, Employee, Hospital, Request, TransfusionCenter
from schemas import DoctorSchema, DonationSchema, DonorSchema, EmployeeSchema, HospitalSchema, RequestSchema, TransfusionCenterSchema


@app.route("/")
def hello():
    tables = ""
    result = db.session.execute("show tables;").fetchall()
    for entry in result:
        tables += str(entry.items()[0][1]) + " "
    return tables


@app.route("/employee", methods=['GET'])
def get_all_employees():
    if request.method == "GET":
        employees = Employee.query.all()
        employee_schema = EmployeeSchema(many=True)
        return jsonify(employee_schema.dump(employees).data)


@app.route("/employee/<int:employeeId>", methods=['GET', 'DELETE'])
def get_employee_by_id(employeeId):
    if request.method == "GET":
        employee = Employee.query.get(employeeId)
        employee_schema = EmployeeSchema()
        return jsonify(employee_schema.dump(employee).data)
    if request.method == "DELETE":
        employee = Employee.query.get(employeeId)
        db.session.delete(employee)
        db.session.commit()
        return jsonify({})


@app.route("/hospital", methods=['GET', 'POST'])
def hospital_api():
    if request.method == "GET":
        hospitals = Hospital.query.all()
        hospital_schema = HospitalSchema(many=True)
        return jsonify(hospital_schema.dump(hospitals).data)
    if request.method == "POST":
        hospital = Hospital(request.args.get('name'))
        db.session.add(hospital)
        db.session.commit()
        return jsonify(hospital.id_hospital)



