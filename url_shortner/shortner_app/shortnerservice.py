from dbapp.dbconns import DbConnection
from django.conf import settings as my_settings


class urlShortnerService:

	def __call__(self,data):
		db_name = my_settings.MONGODB_DB_NAME
		if isinstance(data,dict):
			return self.set_obj(data,db_name)

	def get_connection(self,db_name):
		dbconn = DbConnection()
		return dbconn(my_settings.STORAGE_TYPE)[db_name]

	def exit(self,conn_obj):
		conn_obj.close()
		return True


	def set_obj(self,data,db_name):
		db_connection = self.get_connection(db_name)
		if db_connection:
			print(data)
			data['expiry_time'] = 0
			data['main_url'] = '{}{}'.format(data['prefix_data'],data['frag_url'])
			coll_obj = db_connection['survey']
			obj = coll_obj.insert(data)
			print(data)

