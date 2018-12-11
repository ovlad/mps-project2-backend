import unittest
import json
import requests
import urllib
import test.utils.testutils as testutils

class TestMpsLogin(unittest.TestCase):
	""" Tests for /login """

	endpoint = "/login"
	url = ""
	token = ""

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def _test_get_auth_token(self):
		""" Get valid authentication token """
		(email, password) = testutils.add_donor()

		data = [
		 	("email", email),
		 	("password", password)
		]

		self.url = testutils.make_encoded_url(self.endpoint, data)
		response = requests.post(self.url)
		
		return response.json()["token"]

	def test_login_post_successful(self):
		""" Test successful POST /login """
		self.token = self._test_get_auth_token()

		# Token is valid - not null
		self.assertNotEqual(self.token, "")

	def test_login_post_invalid_params(self):
		""" Test login when given invalid params in query """
		data = [
			("invalid", "params"),
			("password", "incorrect")
		]

		expected = {
			u"message": "Missing `email` param."
		}
		self.url = testutils.make_encoded_url(self.endpoint, data)
		response = requests.post(self.url)

		actual = response.json()["error"]
		self.assertEqual(expected, actual)

	def test_login_get_not_found(self):
		""" Test GET /login not allowed """
		self.url = testutils.make_encoded_url(self.endpoint, [])
		response = requests.get(self.url, verify=False)
		self.assertEqual(response.status_code, 401)

	def test_login_delete_not_found(self):
		""" Test DELETE /login not allowed """
		self.url = testutils.make_encoded_url(self.endpoint, [])
		response = requests.delete(self.url, verify=False)
		self.assertEqual(response.status_code, 401)

	def test_login_put_not_found(self):
		""" Test PUT /login not allowed """
		self.url = testutils.make_encoded_url(self.endpoint, [])
		response = requests.put(self.url, verify=False)
		self.assertEqual(response.status_code, 401)


def suite():
	test_suite = unittest.TestSuite()
	test_suite.addTest(unittest.makeSuite(TestMpsLogin, "test"))
	return test_suite

if __name__ == '__main__':
	unittest.main()