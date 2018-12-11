import unittest
import json
import requests
import urllib
import test.utils.testutils as testutils

headers = {
	"Authorization": "Bearer %s" % testutils.start_session()
}

class TestMpsHospital(unittest.TestCase):
	""" Tests for /hospital """

	endpoint = "/hospital"
	table = "hospital"
	url = ""
	id_hospital = ""

	value = "'testing_hospital'"
	field = "name"
	fetch_condition = "name like 'testing_hospital'"

	def setUp(self):
		testutils.insert_into_db(self.table, self.field, self.value)
		self.url = testutils.URL + self.endpoint

	def tearDown(self):
		testutils.cleanup_database(self.table, self.fetch_condition)

	def test_hospital_get_successful(self):
		""" Test successful GET /hospital """

		response = requests.get(self.url, headers=headers)
		self.assertEqual(response.status_code, 200)

	def test_hospital_get_successful_with_id(self):
		""" Test successful GET /hospital/{id} """
		result = testutils.make_select_query(self.table, "id_hospital",
											self.fetch_condition)

		hospital_id = result[0][0]
		response = requests.get(self.url + '/' + str(hospital_id),
								headers=headers)

		self.assertEqual(response.json()["idHospital"], hospital_id)

	def test_hospital_get_unauthorized_call(self):
		""" Test unauthorized call for GET /hospital """
		result = testutils.make_select_query(self.table, "id_hospital",
											self.fetch_condition)

		hospital_id = result[0][0]
		response = requests.get(self.url + '/' + str(hospital_id))
		expected_status_code = 401

		self.assertEqual(response.status_code, expected_status_code)

	def test_hospital_delete_successful_with_id(self):
		""" Test successful DELETE /hospital{id} """
		result = testutils.make_select_query(self.table,
											"id_hospital",
											self.fetch_condition)

		id_hospital = result[0][0]
		self.url = testutils.URL + self.endpoint + '/' + str(id_hospital)
		response = requests.delete(self.url, headers=headers)	
		
		# Check that the entry was removed from database
		result = testutils.make_select_query(self.table,
											None,
											"id_hospital = %s" % str(id_hospital))
		self.assertEqual(result, ())

	def test_hospital_delete_unauthorized_call(self):
		""" Test unauthorized call for DELETE /hospital{id} """
		result = testutils.make_select_query(self.table,
											"id_hospital",
											self.fetch_condition)

		id_hospital = result[0][0]
		self.url = testutils.URL + self.endpoint + '/' + str(id_hospital)
		response = requests.delete(self.url)
		expected_status_code = 401

		self.assertEqual(response.status_code, expected_status_code)

	def test_hospital_post_successful(self):
		""" Test successful call for POST /hospital """
		params = [
			(self.field, self.value)
		]
		self.url = testutils.make_encoded_url(self.endpoint, params)
		response = requests.post(self.url)

		result = testutils.make_select_query(self.table,
											self.field, self.fetch_condition)
		self.assertIn(result[0][0], self.value)

class TestDb(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_database(self):
		db = testutils.get_db()
		c = db.cursor()
		c.execute('desc employee')
		res = c.fetchall()
		c.close()
		db.close()

		print res


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestMpsHospital, "test"))
    # test_suite.addTest(unittest.makeSuite(TestDb, "test"))
    return test_suite

if __name__ == '__main__':
	unittest.main()
