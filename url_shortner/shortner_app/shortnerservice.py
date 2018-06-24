import copy
from dbapp.dbconns import DbConnection
from django.conf import settings as my_settings
from shortner_utils.utils import UniqueElemUtil , UrlSlugGenerator


class urlShortnerDBService:

	def __call__(self,data):
		db_name = my_settings.MONGODB_DB_NAME
		if isinstance(data,dict):
			return self.main_service(data,db_name)

	def get_connection(self,db_name):
		dbconn = DbConnection()
		return dbconn(my_settings.STORAGE_TYPE)[db_name]

	def exit(self,conn_obj):
		conn_obj.close()
		return True

	def main_service(self,data,db_name,exist = False):
		db_connection = self.get_connection(db_name)
		coll_obj = db_connection['shurlman']

		shurl_data = self.get_obj(data,coll_obj)

		if shurl_data:
			exist = True
			print(shurl_data)
		else:
			shurl_data = copy.deepcopy(data)
			shurl_data['seq_id'] = self.get_nextseq_num('seqid',db_connection['seqcounter'])
			shurl_data['key_id'] = UniqueElemUtil.uniid_key(int(shurl_data['seq_id']))

		shurl_slug = self.getShurlSlug(int(shurl_data['key_id']))
		if not exist:
			self.set_obj(shurl_data,coll_obj)
		return shurl_slug , exist


	def get_obj(self,data,collection_conn):
		main_url = '{}{}'.format(data['prefix_data'],data['frag_url'])
		return collection_conn.find_one({'main_url':main_url})

	def get_nextseq_num(self,seq_name,collection_conn):
		next_seq_doc = collection_conn.find_one_and_update({
			'_id': seq_name },
			{'$inc': {'sequence_val': 1}},
			upsert = False
			)
		return int(next_seq_doc['sequence_val'])


	def set_obj(self,data,collection_conn):
		if collection_conn:
			data['expiry_time'] = 0
			data['main_url'] = '{}{}'.format(data['prefix_data'],data['frag_url'])
			obj = collection_conn.insert(data)
			return data

	def getShurlSlug(self,key):
		return UrlSlugGeneratorService.generateSlug(int(key))


class UrlSlugGeneratorService:

	@staticmethod
	def generateSlug(key):
		shurl_slug = UrlSlugGenerator.generateSlug(key)
		return shurl_slug


