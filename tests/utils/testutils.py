import MySQLdb
import MySQLdb.cursors
import urllib
import requests

# Production URL
URL = "http://35.188.36.73"
#URL = "http://localhost:7777"

headers = {
	"Content-type": "application/json"
}

def make_encoded_url(endpoint, query_params):
	""" Return encoded url with query params """
	return URL + endpoint + "?" + urllib.urlencode(query_params)

def get_db():
	""" Get db instance """
	return MySQLdb.connect(
		host="mps2db.mysql.database.azure.com",
		user="mps2admin@mps2db",
		passwd="ParolaSecure1!",
		db="mps2project",
		cursorclass=MySQLdb.cursors.Cursor)

def cleanup_database(table, fetch_condition):
	""" Delete value searched by fetch_condition from table """
	db = get_db()
	c = db.cursor()
	c.execute('DELETE FROM {} WHERE {}'.format(
				table, fetch_condition))
	c.close()
	db.commit()
	db.close()

def make_select_query(table, fields=None, condition=None):
	""" Make select query from db """
	db = get_db()
	c = db.cursor()
	if condition and fields:
		c.execute('SELECT {} FROM {} WHERE {}'.format(
					fields, table, condition))
	elif fields:
		c.execute('SELECT {} FROM {}'.format(fields, table))
	elif condition:
		c.execute('SELECT * FROM {} WHERE {}'.format(table, condition))
	else:
		c.execute('SELECT * FROM {}'.format(table))

	result = c.fetchall()
	return result

def insert_into_db(table, fields, values):
	""" Run SQL insert """
	db = get_db()
	c = db.cursor()

	c.execute('INSERT INTO {}({}) VALUES ({})'.format(
				table, fields, values))

	c.close()
	db.commit()
	db.close()

def add_donor():
	""" Add donor for testing and return email and password """
	fields = "name, surname, mail, password, blood_type, Rh"
	values = "'auto', 'testing', 'test@ex.com', 'pass', '0', 'positive'"

	db = get_db()
	c = db.cursor()
	c.execute("INSERT INTO donor({}) values({})".format(fields, values))

	c.close()
	db.commit()
	db.close()
	return ('test@ex.com', 'pass')

def start_session():
	""" Login user with email and password and return token """
	(email, password) = add_donor()
	params = [
		("email", email),
		("password", password)
	]

	url = make_encoded_url('/login', params)
	response = requests.post(url)
	cleanup_database("donor", "mail like '%s'" % email)

	return response.json()["token"]
