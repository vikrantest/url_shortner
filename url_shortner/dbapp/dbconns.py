import sys
from pymongo import MongoClient
from django.conf import settings as my_settings




class DbConnection(object):

	def __call__(self,storage_type):
		if storage_type == 'mongo':
			return self.mongo_db_connect()
		else:
			return None

	"""
	Mongodb conneciton class and other db conneciton is commented as we are not using
	"""


	"""
	def redis_db_connect(self,host=None,username=None,password=None,database=None):
		stocons = self.stocons
		_host = host or stocons.REDIS_DATABASE_HOST
		_password = password or stocons.REDIS_DATABASE_PASSWORD
		_database = database or 0
		_port = stocons.REDIS_PORT
		print _host,_port,_password

		try:
			if _password:
				connection = redis.Redis(host= _host, port= _port, db= _database,password= 'vh6HSwa9')
			else:
				connection = redis.Redis(host= _host, port= _port, db= _database)
			return connection
		except:
			print "Error while connecting redis server db"
			return None



	def postgres_db_connect(self,host=None,username=None,password=None,database=None):
		_host = host or LOCALHOST
		_username = username
		_password = password
		_database = database

		try:
			connection = psycopg2.connect("host=_host,username=_username,password=_password,database=_database")
			return connection
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			return None

	def mysql_db_connect(self,host=None,username=None,password=None,database=None):
		_host = host or LOCALHOST
		_username = username
		_password = password
		_database = database

		try:
			connection = MySQLdb.connect(_host,_username,_password,_database)
			return connection
		except MySQLdb.Error, e:
			print("Error %d: %s" % (e.args[0], e.args[1]))
			return None

	"""


	def mongo_db_connect(self):#check for username and password
		__host = my_settings.MONGODB_HOST
		__port = my_settings.MONGODB_PORT or 27017
		__username = my_settings.MONGODB_USERNAME
		__password = my_settings.MONGODB_PASSWORD
		url = '%s:%s' % (__host,__port)

		try:
			if any([__username is None,__password is None ]):
				connection = MongoClient(url,connect=False)

			else:
				connection = MongoClient(__host,username=__username,password=__password,connect=False)
			return connection
		except:# raise proper exception
			print("Error while connecting mongo db")
			return None

		
	



