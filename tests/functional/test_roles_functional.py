import unittest
import json
import requests
import urllib
import test.utils.testutils as testutils

headers = {
	"Authorization": "Bearer %s" % testutils.start_session()
}

class TestMpsDonor(unittest.TestCase):
	""" Tests for /donor endpoint """

	endpoint = "/donor"
	table = "donor"
	url = ""

	data = {
		"fields": "name, surname, mail, password, blood_type, Rh",
		"values": "'admin', 'testing', 'test@admin.com', 'pass', '0', 'negative'",
		"fetch_condition": "name like 'admin'"
	}

	def setUp(self):
		testutils.insert_into_db(self.table, self.data["fields"], 
								self.data["values"])

	def tearDown(self):
		testutils.cleanup_database(self.table, self.data["fetch_condition"])

	def test_donor_get_successful(self):
		""" Test successful GET /donor """
		self.url = testutils.URL + self.endpoint
		response = requests.get(self.url, headers=headers)
		
		self.assertEqual(response.status_code, 200)

		# There should be at least one donor inside the database
		self.assertNotEqual(response.json(), {})

	def test_donor_get_unauthorized(self):
		""" Test that GET /donor without token is not authorized """
		self.url = testutils.URL + self.endpoint
		response = requests.get(self.url, verify=False)
		self.assertEqual(response.status_code, 401)

	def test_donor_get_successful_spec_id(self):
		""" Test successful GET /donor{id} """
		result = testutils.make_select_query(self.table,
											"id_donor",
											self.data["fetch_condition"])
		id_donor = result[0][0]
		self.url = testutils.URL + self.endpoint + '/' + str(id_donor)
		response = requests.get(self.url, headers=headers)
		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()["id_donor"], id_donor)

	def test_donor_get_invalid_id(self):
		""" Test GET /donor{id} with invalid id """
		id_donor = "invalid"
		expected = {
			u"message": u"Invalid donor id %s" % id_donor
		}
		self.url = testutils.URL + self.endpoint + '/' + str(id_donor)
		response = requests.get(self.url, headers=headers)
		actual = response.json()["error"]

		self.assertEqual(expected, actual)

	def test_donor_delete_successful_spec_id(self):
		""" Test successful DELETE /donor{id} """
		result = testutils.make_select_query(self.table,
											"id_donor",
											self.data["fetch_condition"])

		id_donor = result[0][0]
		self.url = testutils.URL + self.endpoint + '/' + str(id_donor)
		response = requests.delete(self.url, headers=headers)	
		
		# Check that the entry was removed from database
		result = testutils.make_select_query(self.table,
											None,
											"id_donor = %s" % str(id_donor))
		self.assertEqual(result, ())

	def test_donor_delete_invalid_id(self):
		""" Test DELETE /donor{id} when id is invalid """
		id_donor = "invalid"
		expected = {
			u"message": u"No data was deleted"
		}

		self.url = testutils.URL + self.endpoint + '/' + id_donor
		response = requests.delete(self.url, headers=headers)
		actual = response.json()["error"]
		
		self.assertEqual(expected, actual)

	def test_donor_post_not_found(self):
		""" Test error on POST /donor """
		data = {
			"invalid": "param"
		}
		self.url = testutils.URL + self.endpoint
		response = requests.post(self.url, data=json.dumps(data), headers=headers)
		self.assertEqual(response.status_code, 404)

	def test_donor_put_not_found(self):
		""" Test error on PUT /donor """
		data = {
			"invalid": "param"
		}
		self.url = testutils.URL + self.endpoint
		response = requests.put(self.url, data=json.dumps(data), headers=headers)
		self.assertEqual(response.status_code, 404)


class TestMpsDoctor(unittest.TestCase):
	""" Tests for /doctor endpoint """	

	endpoint = "/doctor"
	table = "doctor"
	url = ""

	data = {
		"fields": "name, surname, mail, password, is_active, id_hospital",
		"values": "'doc', 'testing', 'test@doctor.com', 'pass', '1', '2'",
		"fetch_condition": "name like 'doc'"
	}

	def setUp(self):
		testutils.insert_into_db(self.table, self.data["fields"], 
								self.data["values"])

	def tearDown(self):
		testutils.cleanup_database(self.table, self.data["fetch_condition"])

	def test_doctor_get_successful(self):
		""" Test successful GET /doctor """
		self.url = testutils.URL + self.endpoint
		response = requests.get(self.url, headers=headers)
		
		self.assertEqual(response.status_code, 200)

		# There should be at least one donor inside the database
		self.assertNotEqual(response.json(), {})

	def test_doctor_get_unauthorized(self):
		""" Test that GET /doctor without token is not authorized """
		self.url = testutils.URL + self.endpoint
		response = requests.get(self.url, verify=False)
		self.assertEqual(response.status_code, 401)

	def test_doctor_get_successful_spec_id(self):
		""" Test successful GET /doctor{id} """
		result = testutils.make_select_query(self.table,
											"id_doctor",
											self.data["fetch_condition"])
		id_doctor = result[0][0]
		self.url = testutils.URL + self.endpoint + '/' + str(id_doctor)
		response = requests.get(self.url, headers=headers)
		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()["id_doctor"], id_doctor)


	def test_doctor_get_invalid_id(self):
		""" Test GET /doctor{id} with invalid id """
		id_doctor = "invalid"
		expected = {
			u"message": u"Invalid doctor id %s" % id_doctor
		}
		self.url = testutils.URL + self.endpoint + '/' + str(id_doctor)
		response = requests.get(self.url, headers=headers)
		actual = response.json()["error"]

		self.assertEqual(expected, actual)

	def test_doctor_delete_successful_spec_id(self):
		""" Test successful DELETE /doctor{id} """
		result = testutils.make_select_query(self.table,
											"id_doctor",
											self.data["fetch_condition"])

		id_doctor = result[0][0]
		self.url = testutils.URL + self.endpoint + '/' + str(id_doctor)
		response = requests.delete(self.url, headers=headers)	
		
		# Check that the entry was removed from database
		result = testutils.make_select_query(self.table,
											None,
											"id_doctor = %s" % str(id_doctor))
		self.assertEqual(result, ())

	def test_doctor_delete_invalid_id(self):
		""" Test DELETE /doctor{id} when id is invalid """
		id_doctor = "invalid"
		expected = {
			u"message": u"No data was deleted"
		}

		self.url = testutils.URL + self.endpoint + '/' + id_doctor
		response = requests.delete(self.url, headers=headers)
		actual = response.json()["error"]
		
		self.assertEqual(expected, actual)


	def test_doctor_post_not_found(self):
		""" Test error on POST /doctor """
		data = {
			"invalid": "param"
		}
		self.url = testutils.URL + self.endpoint
		response = requests.post(self.url, data=json.dumps(data), headers=headers)
		self.assertEqual(response.status_code, 404)

	def test_doctor_put_not_found(self):
		""" Test error on PUT /doctor """
		data = {
			"invalid": "param"
		}
		self.url = testutils.URL + self.endpoint
		response = requests.put(self.url, data=json.dumps(data), headers=headers)
		self.assertEqual(response.status_code, 404)


class TestMpsEmployee(unittest.TestCase):
	""" Tests for /employee endpoint """	

	endpoint = "/employee"
	table = "employee"
	url = ""

	data = {
		"fields": "name, surname, mail, password, is_active, id_center",
		"values": "'emp', 'testing', 'test@doctor.com', 'pass', '1', '2'",
		"fetch_condition": "name like 'emp'"
	}

	def setUp(self):
		testutils.insert_into_db(self.table, self.data["fields"], 
								self.data["values"])

	def tearDown(self):
		testutils.cleanup_database(self.table, self.data["fetch_condition"])

	def test_employee_get_successful(self):
		""" Test successful GET /employee """
		self.url = testutils.URL + self.endpoint
		response = requests.get(self.url, headers=headers)
		
		self.assertEqual(response.status_code, 200)

		# There should be at least one donor inside the database
		self.assertNotEqual(response.json(), {})

	@unittest.skip('s')
	def test_employee_get_unauthorized(self):
		""" Test that GET /employee without token is not authorized """
		self.url = testutils.URL + self.endpoint
		response = requests.get(self.url, verify=False)
		self.assertEqual(response.status_code, 401)

	def test_employee_get_successful_spec_id(self):
		""" Test successful GET /doctor{id} """
		result = testutils.make_select_query(self.table,
											"id_employee",
											self.data["fetch_condition"])
		id_employee = result[0][0]
		self.url = testutils.URL + self.endpoint + '/' + str(id_employee)
		response = requests.get(self.url, headers=headers)
		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()["idEmployee"], id_employee)


	def test_employee_get_invalid_id(self):
		""" Test GET /employee{id} with invalid id """
		id_employee = "1432"
		self.url = testutils.URL + self.endpoint + '/' + str(id_employee)
		response = requests.get(self.url, headers=headers)
		self.assertEqual(response.json(), {})


	def test_employee_post_not_found(self):
		""" Test error on POST /employee """
		data = {
			"invalid": "param"
		}
		self.url = testutils.URL + self.endpoint
		response = requests.post(self.url, data=json.dumps(data), headers=headers)
		self.assertEqual(response.status_code, 405)

	def test_employee_put_not_found(self):
		""" Test error on PUT /employee """
		data = {
			"invalid": "param"
		}
		self.url = testutils.URL + self.endpoint
		response = requests.put(self.url, data=json.dumps(data), headers=headers)
		self.assertEqual(response.status_code, 405)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestMpsDonor, "test"))
    test_suite.addTest(unittest.makeSuite(TestMpsDoctor, "test"))
    test_suite.addTest(unittest.makeSuite(TestMpsEmployee, "test"))
    return test_suite

if __name__ == '__main__':
	unittest.main()