from server import app, db
from flask import request, jsonify
from models import Doctor, Donation, Donor, Employee, Hospital, Request, TransfusionCenter
from schemas import DoctorSchema, DonationSchema, DonorSchema, EmployeeSchema, HospitalSchema, RequestSchema, TransfusionCenterSchema


# @app.route("/")
# def hello():
#     tables = ""
#     result = db.session.execute("show tables;").fetchall()
#     for entry in result:
#         tables += str(entry.items()[0][1]) + " "
#     return tables
#

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

@app.route("/hospital/<int:hospitalId>", methods=['GET', 'DELETE', 'PUT'])
def get_hospital_by_id(hospitalId):
    if request.method == "GET":
        hospital = Hospital.query.get(hospitalId)
        hospital_schema = HospitalSchema()
        return jsonify(hospital_schema.dump(hospital).data)
    if request.method == "DELETE":
        hospital = Hospital.query.get(hospitalId)
        db.session.delete(hospital)
        db.session.commit()
        return jsonify({})
    if request.method == "PUT":
        hospital = Hospital.query.get(hospitalId)
        hospital.name = request.args.get('name')
        db.session.commit()
        return jsonify(hospital.id_hospital)


@app.route("/transfusionCenter", methods=['GET', 'POST'])
def transfusion_api():
    if request.method == "GET":
        transfusion_c = TransfusionCenter.query.all()
        transfusion_c_schema = TransfusionCenterSchema(many=True)
        return jsonify(transfusion_c_schema.dump(transfusion_c).data)
    if request.method == "POST":
        transfusion = TransfusionCenter(request.args.get('name'))
        db.session.add(transfusion)
        db.session.commit()
        return jsonify(transfusion.id_center)

@app.route("/transfusionCenter/<int:transfusionCenterId>", methods=['GET', 'DELETE', 'PUT'])
def get_transfusionCenter_by_id(transfusionCenterId):
    if request.method == "GET":
        transfusion_c = TransfusionCenter.query.get(transfusionCenterId)
        transfusion_c_schema = TransfusionCenterSchema()
        return jsonify(transfusion_c_schema.dump(transfusion_c).data)
    if request.method == "DELETE":
        transfusion_c = TransfusionCenter.query.get(transfusionCenterId)
        db.session.delete(transfusion_c)
        db.session.commit()
        return jsonify({})
    if request.method == "PUT":
        transfusion_c = TransfusionCenter.query.get(transfusionCenterId)
        transfusion_c.name = request.args.get('name')
        db.session.commit()
        return jsonify(transfusion_c.name)

#Should implement GET, POST, PUT request with optional params


@app.route("/request/<int:requestId>", methods=['GET', 'DELETE'])
def get_request_by_id(requestId):
    if request.method == "GET":
        request_x = Request.query.get(requestId)
        request_schema = RequestSchema()
        return jsonify(request_schema.dump(request_x).data)
    if request.method == "DELETE":
        request_x = Request.query.get(requestId)
        db.session.delete(request_x)
        db.session.commit()
        return jsonify({})


#Should implement GET, POST, PUT donation with optional params
#
# @app.route("/donation", methods=['GET', 'POST'])
# def get_donation():
#     if request.method == "GET":
#         donation = Donation.query.filter_by()
#         donation_schema = DonationSchema(many=True)
#         return jsonify(donation_schema.dump(donation).data)
#     if request.method == "POST":
#         donation = Donation(request.args.get('name'))
#         db.session.add(donation)
#         db.session.commit()
#         return jsonify(donation.id_donation)


@app.route("/donation/<int:donationId>", methods=['GET', 'DELETE'])
def get_donation_by_id(donationId):
    if request.method == "GET":
        donation = Donation.query.get(donationId)
        donation_schema = DonationSchema()
        return jsonify(donation_schema.dump(donation).data)
    if request.method == "DELETE":
        donation = Request.query.get(donationId)
        db.session.delete(donation)
        db.session.commit()
        return jsonify({})

