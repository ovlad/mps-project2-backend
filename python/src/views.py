from server import app
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


@app.route("/donor", methods=['GET'])
def donor_api():
    if request.method == "GET":
        donors = Donor.query.all()
        donor_schema = DonorSchema(many=True)
        output = donor_schema.dump(donors).data
        return jsonify(output)



