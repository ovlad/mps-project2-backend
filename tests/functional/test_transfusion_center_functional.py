import unittest
import json
import requests
import urllib
import test.utils.testutils as testutils

headers = {
	"Authorization": "Bearer %s" % testutils.start_session()
}

class TestMpsTransfusionCenter(unittest.TestCase):
	""" Tests for /hospital """

	endpoint = "/transfusionCenter"
	table = "transfusion_center"
	url = ""
	id_center = ""

	value = "'testing_center'"
	field = "name"
	fetch_condition = "name like 'testing_center'"

	def setUp(self):
		testutils.insert_into_db(self.table, self.field, self.value)
		self.url = testutils.URL + self.endpoint

	def tearDown(self):
		testutils.cleanup_database(self.table, self.fetch_condition)

	def test_transfusion_center_get_successful(self):
		""" Test successful GET /transfusionCenter """

		response = requests.get(self.url, headers=headers)
		self.assertEqual(response.status_code, 200)

	def test_transfusion_center_get_successful_with_id(self):
		""" Test successful GET /transfusionCenter/{id} """
		result = testutils.make_select_query(self.table, "id_center",
											self.fetch_condition)

		id_center = result[0][0]
		response = requests.get(self.url + '/' + str(id_center),
								headers=headers)

		self.assertEqual(response.json()["idCenter"], id_center )

	def test_transfusion_center_get_unauthorized_call(self):
		""" Test unauthorized call for GET /transfusionCenter """
		result = testutils.make_select_query(self.table, "id_center",
											self.fetch_condition)

		id_center = result[0][0]
		response = requests.get(self.url + '/' + str(id_center))
		expected_status_code = 401

		self.assertEqual(response.status_code, expected_status_code)

	def test_transfusion_center_delete_successful_with_id(self):
		""" Test successful DELETE /transfusionCenter{id} """
		result = testutils.make_select_query(self.table,
											"id_center",
											self.fetch_condition)

		id_center = result[0][0]
		self.url = testutils.URL + self.endpoint + '/' + str(id_center)
		response = requests.delete(self.url, headers=headers)	
		
		# Check that the entry was removed from database
		result = testutils.make_select_query(self.table,
											None,
											"id_center = %s" % str(id_center))
		self.assertEqual(result, ())

	def test_transfusion_center_delete_unauthorized_call(self):
		""" Test unauthorized call for DELETE /transfusionCenter{id} """
		result = testutils.make_select_query(self.table,
											"id_center",
											self.fetch_condition)

		id_center = result[0][0]
		self.url = testutils.URL + self.endpoint + '/' + str(id_center)
		response = requests.delete(self.url)
		expected_status_code = 401

		self.assertEqual(response.status_code, expected_status_code)

	def test_transfusion_center_post_successful(self):
		""" Test successful call for POST /transfusionCenter """
		params = [
			(self.field, self.value)
		]
		self.url = testutils.make_encoded_url(self.endpoint, params)
		response = requests.post(self.url)

		result = testutils.make_select_query(self.table,
											self.field, self.fetch_condition)
		self.assertIn(result[0][0], self.value)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestMpsTransfusionCenter, "test"))
    return test_suite

if __name__ == '__main__':
	unittest.main()
