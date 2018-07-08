import sys
import os
from django.conf import settings as my_settings
from dbapp.dbconns import DbConnection

class DbOperations:

	operation_collections = {'generate_url':'shurlman','sequence_coll':'seqcounter','get_redirect_main_url':'shurlman'}
	db_name = my_settings.MONGODB_DB_NAME

	@classmethod
	def getConnection(cls,db_connection_obj=None,operation=None):
		if not db_connection_obj:
			db_connection = DbConnection()
			db_connection_obj = db_connection(my_settings.STORAGE_TYPE)[cls.db_name]
		if operation and operation in cls.operation_collections.keys():
			return cls.getCollectionsConnection(db_connection_obj,operation)
		else:
			return db_connection_obj

	@classmethod
	def createCollection(cls,connections):
		pass

	@classmethod
	def getCollectionsConnection(cls,db_connection,operation):
		return db_connection[cls.operation_collections[operation]]
