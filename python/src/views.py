from server import app, db
from flask import request, jsonify
from models import Donation, Employee, Hospital, Request, TransfusionCenter
from schemas import DonationSchema, EmployeeSchema, HospitalSchema, RequestSchema, TransfusionCenterSchema
from enums import RequestStatusEnum, DonorRhEnum
from datetime import datetime


@app.route("/employee", methods=['GET'], defaults={'employeeId': None})
@app.route("/employee/<int:employeeId>", methods=['GET', 'DELETE'])
def employee_api(employeeId):
    employee_schema = EmployeeSchema()
    employee_schema_many = EmployeeSchema(many=True)

    if request.method == "GET":
        if employeeId:
            employee = Employee.query.get(employeeId)
            return jsonify(employee_schema.dump(employee).data)
        else:
            employees = Employee.query.all()
            return jsonify(employee_schema_many.dump(employees).data)

    if request.method == "DELETE":
        if employeeId:
            employee = Employee.query.get(employeeId)
            db.session.delete(employee)
            db.session.commit()
            return jsonify({})


@app.route("/hospital", methods=['GET'], defaults={"hospitalId": None})
@app.route("/hospital/<int:hospitalId>", methods=['GET'])
def hospital_api_unprotected(hospitalId):
    hospital_schema_many = HospitalSchema(many=True)
    hospital_schema = HospitalSchema()

    if request.method == "GET":
        if hospitalId:
            hospital = Hospital.query.get(hospitalId)
            return jsonify(hospital_schema.dump(hospital).data)
        else:
            hospitals = Hospital.query.all()
            return jsonify(hospital_schema_many.dump(hospitals).data)


@app.route("/hospital", methods=['POST'], defaults={'hospitalId': None})
@app.route("/hospital/<int:hospitalId>", methods=['PUT', 'DELETE'])
def hospital_api(hospitalId):
    hospital_schema = HospitalSchema()
    if request.method == "POST":
        hospital = Hospital(request.args.get('name'))
        db.session.add(hospital)
        db.session.commit()
        return jsonify(hospital_schema.dump(hospital).data)

    if request.method == "PUT":
        if hospitalId:
            hospital = Hospital.query.get(hospitalId)
            hospital.name = request.args.get('name')
            db.session.commit()
            return jsonify(hospital_schema.dump(hospital).data)

    if request.method == "DELETE":
        if hospitalId:
            hospital = Hospital.query.get(hospitalId)
            db.session.delete(hospital)
            db.session.commit()
            return jsonify({})


@app.route("/transfusionCenter", methods=['GET'], defaults={'transfusionCenterId': None})
@app.route("/transfusionCenter/<int:transfusionCenterId>", methods=['GET'])
def transfusion_center_api_unprotected(transfusionCenterId):
    transfusion_center_schema = TransfusionCenterSchema()
    transfusion_center_schema_many = TransfusionCenterSchema(many=True)

    if request.method == "GET":
        if transfusionCenterId:
            transfusion_center = TransfusionCenter.query.get(transfusionCenterId)
            return jsonify(transfusion_center_schema.dump(transfusion_center).data)
        else:
            transfusion_centers = TransfusionCenter.query.all()
            return jsonify(transfusion_center_schema_many.dump(transfusion_centers).data)


@app.route("/transfusionCenter", methods=['POST'], defaults={'transfusionCenterId': None})
@app.route("/transfusionCenter/<int:transfusionCenterId>", methods=['PUT', 'DELETE'])
def transfusion_center_api(transfusionCenterId):
    transfusion_center_schema = TransfusionCenterSchema()
    if request.method == "POST":
        transfusion_center = TransfusionCenter(request.args.get('name'))
        db.session.add(transfusion_center)
        db.session.commit()
        return jsonify(transfusion_center_schema.dump(transfusion_center).data)

    if request.method == "PUT":
        if transfusionCenterId:
            transfusion_center = TransfusionCenter.query.get(transfusionCenterId)
            transfusion_center.name = request.args.get('name')
            db.session.commit()
            return jsonify(transfusion_center_schema.dump(transfusion_center).data)

    if request.method == "DELETE":
        if transfusionCenterId:
            transfusion_center = TransfusionCenter.query.get(transfusionCenterId)
            db.session.delete(transfusion_center)
            db.session.commit()
            return jsonify({})


@app.route("/bloodRequest", methods=['GET', 'POST'], defaults={'requestId': None})
@app.route("/bloodRequest/<int:requestId>", methods=['GET', 'PUT', 'DELETE'])
def request_api(requestId):
    request_schema = RequestSchema()
    request_schema_many = RequestSchema(many=True)

    if request.method == "GET":
        if requestId:
            request_single = Request.query.cte(requestId)
            return jsonify(request_schema.dump(request_single).data)
        else:
            request_many = Request.query.all()
            request_result = list(request_many)
            for entry in request.args:
                for request_one in request_many:
                    left = str(request.args.get(entry))
                    if entry == "rh":
                        try:
                            right = str(getattr(request_one, entry).value)
                        except AttributeError:
                            right = None
                    else:
                        right = str(getattr(request_one, entry))
                    if left != right:
                        try:
                            request_result.remove(request_one)
                        except ValueError:
                            continue
            return jsonify(request_schema_many.dump(request_result).data)

    if request.method == "POST":
        receiving_person = request.args.get('receivingPerson')
        quantity = request.args.get('quantity')
        blood_type = request.args.get('bloodType')
        rh = request.args.get('rh')
        doctor_id = request.args.get('doctorId')
        transfusion_center_id = request.args.get('transfusionCenterId')
        new_request = Request(blood_type, rh, receiving_person, quantity, doctor_id, transfusion_center_id)
        db.session.add(new_request)
        db.session.commit()
        return jsonify(request_schema.dump(new_request).data)

    if request.method == "PUT":
        if requestId:
            request_one = Request.query.get(requestId)
            request_one.status = request.args.get('status')
            request_one.receiving_person = request.args.get('receivingPerson')
            request_one.quantity = request.args.get('quantity')
            request_one.bloodtype = request.args.get('bloodType')
            request_one.rh = request.args.get('rh')
            request_one.idDoctor = request.args.get('doctorId')
            request_one.idCenter = request.args.get('transfusionCenterId')
            db.session.commit()
            return jsonify(request_schema.dump(request_one).data)

    if request.method == "DELETE":
        request_x = Request.query.get(requestId)
        db.session.delete(request_x)
        db.session.commit()
        return jsonify({})


@app.route("/donation", methods=['GET', 'POST'], defaults={'donationId': None})
@app.route("/donation/<int:donationId>", methods=['GET', 'PUT', 'DELETE'])
def donation_api(donationId):
    donation_schema = DonationSchema()
    donation_schema_many = DonationSchema(many=True)

    if request.method == "GET":
        if donationId:
            donation = Donation.query.get(donationId)
            return jsonify(donation_schema.dump(donation).data)
        else:
            donation_many = Donation.query.all()
            donation_result = list(donation_many)
            for entry in request.args:
                for donation_one in donation_many:
                    if str(request.args.get(entry)) != str(getattr(donation_one, entry)):
                        try:
                            donation_result.remove(donation_one)
                        except ValueError:
                            continue
            return jsonify(donation_schema_many.dump(donation_result).data)

    if request.method == "POST":
        quantity = request.args.get('quantity')
        date = request.args.get('date')
        formatted_date = datetime.strptime(date, "%d/%m/%Y")
        donor_id = request.args.get('donorId')
        request_id = request.args.get('requestId')
        blood_test = request.get_data()
        new_donation = Donation(blood_test, formatted_date, quantity, donor_id, request_id)
        db.session.add(new_donation)
        db.session.commit()
        return jsonify(donation_schema.dump(new_donation).data)

    if request.method == "PUT":
        if donationId:
            donation_one = Donation.query.get(donationId)
            donation_one.quantity = request.args.get('quantity')
            formatted_date = datetime.strptime(request.args.get('date'), "%d/%m/%Y")
            donation_one.date = formatted_date
            donation_one.idDonor = request.args.get('donorId')
            donation_one.idRequest = request.args.get('requestId')
            db.session.commit()
            return jsonify(donation_schema.dump(donation_one).data)

    if request.method == "DELETE":
        donation = Donation.query.get(donationId)
        db.session.delete(donation)
        db.session.commit()
        return jsonify({})
