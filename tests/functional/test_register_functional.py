import unittest
import json
import requests
import urllib
import test.utils.testutils as testutils

class TestMpsRegister(unittest.TestCase):
	""" Tests for /register endpoint """

	endpoint = "/register"
	url = ""
	fetch_condition = ""
	params = [
		("email", "test@user.com"),
		("password", "pass"),
		("passwordConfirm", "pass"),
		("role", "DONOR"),
		("name", "Testing"),
		("surname", "User"),
		("bloodType", "0"),
		("rh", "positive"),
		("hospitalId", "2"),
		("transfusionCenterId", "2")
	]
	table = "donor"
	fetch_condition = "name like 'Testing'"

	def setUp(self):
		pass

	def tearDown(self):
		testutils.cleanup_database(self.table, self.fetch_condition)

	def _test_make_uncoded_url(self, query_params):
		""" Returns encoded URL with query params """
		return testutils.URL + self.endpoint + "?" + urllib.urlencode(query_params)

	def test_register_post_successful(self):
		""" Test for a successful POST /register """
		self.url = self._test_make_uncoded_url(self.params)

		response = requests.post(self.url)
		self.assertEqual(response.status_code, 200)

		id_donor = response.json()["id_donor"]
		result = testutils.make_select_query(self.table, "id_donor", self.fetch_condition)
		self.assertEqual(result[0][0], id_donor)

	def test_register_missing_params(self):
		""" Test for missing params when calling POST /register """
		expected = {
			u"message": u"Missing `name` param."
		}

		self.url = self._test_make_uncoded_url(self.params[:4])

		response = requests.post(self.url)
		actual = response.json()["error"]
		self.assertEqual(expected, actual)

	def test_register_invalid_param(self):
		""" Test for invalid params when calling POST /register """
		expected = {
			u"message": u"Missing `surname` param."
		}

		query_params = self.params[:5]
		query_params.append(("srnme", "UNDEFINED"))
		query_params.extend(self.params[6:])
		self.url = self._test_make_uncoded_url(query_params)

		response = requests.post(self.url)
		actual = response.json()["error"]
		self.assertEqual(expected, actual)

	def test_register_get_not_found(self):
		""" Test that DELETE /register is not found """
		self.url = testutils.URL + self.endpoint
		response = requests.delete(self.url, verify=False)
		self.assertEqual(response.status_code, 401)

	def test_register_put_not_found(self):
		""" Test that put /register is not found """
		self.url = self._test_make_uncoded_url(self.params)
		response = requests.put(self.url)
		self.assertEqual(response.status_code, 401)

	def test_register_delete_not_found(self):
		""" Test that GET /register is not found """
		self.url = testutils.URL + self.endpoint
		response = requests.get(self.url, verify=False)
		self.assertEqual(response.status_code, 401)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestMpsRegister, "test"))
    return test_suite

if __name__ == '__main__':
	unittest.main()