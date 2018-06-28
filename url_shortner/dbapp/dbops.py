import sys
import os
from django.conf import settings as my_settings
from dbapp.dbconns import DbConnection

class DbOperations:

	operation_collections = {'generate_url':'shurlman','sequence_coll':'seqcounter','get_redirect_main_url':'shurlman'}
	db_name = my_settings.MONGODB_DB_NAME

	@classmethod
	def getConnection(cls,db_connection_obj=None,operation=None):
		print(operation,cls.operation_collections.keys())

		if not db_connection_obj:
			db_connection = DbConnection()
			db_connection_obj = db_connection(my_settings.STORAGE_TYPE)[cls.db_name]
		if operation and operation in cls.operation_collections.keys():
			print('hre++++++++++++++++')
			return cls.getCollectionsConnection(db_connection_obj,operation)
		else:
			print('there++++++++++++++++++')
			return db_connection_obj

	@classmethod
	def createCollection(cls,connections):
		print(connections)

	@classmethod
	def getCollectionsConnection(cls,db_connection,operation):
		print(cls.operation_collections[operation],'+++++++++++++++end')
		return db_connection[cls.operation_collections[operation]]
