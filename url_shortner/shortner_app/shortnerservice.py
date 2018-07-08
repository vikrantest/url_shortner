import copy
import re
from django.conf import settings as my_settings
from dbapp.dbops import DbOperations
from shortner_utils.utils import UniqueElemUtil , UrlSlugService


class urlShortnerDBService:

	def __call__(self,data):
		db_name = my_settings.MONGODB_DB_NAME
		if isinstance(data,dict):
			return self.generatorService(data,db_name)
		if isinstance(data,str):
			return self.urlGetterService(data,db_name)

	def exit(self,conn_obj):
		conn_obj.close()
		return True

	def getCollectionConn(self,action):
		return DbOperations.getConnection(operation=action)

	def urlGetterService(self,data,db_name):
		db_connection = self.getCollectionConn('get_redirect_main_url')
		key = UrlSlugOperationService.getSlugUrl(data)
		data = db_connection.find_one({'key_id':str(key)})
		if re.match('http',data['main_url']):
			return data['main_url']
		else:
			return 'http://'+data['main_url']

	def generatorService(self,data,db_name,exist = False):
		db_connection = self.getCollectionConn('generate_url')

		shurl_obj_list = self.getObj(data,db_connection)

		print(shurl_obj_list.count())

		shurl_data = shurl_obj_list[0] if shurl_obj_list.count()>0 else None
		if shurl_data and not data['new_shurl']:
			exist = True
		else:
			shurl_data = copy.deepcopy(data)
			shurl_data['seq_id'] = self.getNextseqNum('seqid',self.getCollectionConn('sequence_coll'))
			shurl_data['key_id'] = UniqueElemUtil.uniid_key(int(shurl_data['seq_id']))

		shurl_slug = self.getShurlSlug(int(shurl_data['key_id']))
		if not exist:
			self.setObj(shurl_data,db_connection)
		return shurl_slug , exist


	def getObj(self,data,collection_conn):
		main_url = '{}{}'.format(data['prefix_data'],data['frag_url'])
		return collection_conn.find({'main_url':main_url}).sort([('seq_id',-1)]).limit(1)

	def getNextseqNum(self,seq_name,collection_conn):
		next_seq_doc = collection_conn.find_one_and_update({
			'_id': seq_name },
			{'$inc': {'sequence_val': 1}},
			upsert = False
			)
		return int(next_seq_doc['sequence_val'])


	def setObj(self,data,collection_conn):
		if collection_conn:
			data['expiry_time'] = 0
			data['main_url'] = '{}{}'.format(data['prefix_data'],data['frag_url'])
			obj = collection_conn.insert(data)
			return data

	def getShurlSlug(self,key):
		return UrlSlugOperationService.generateSlug(int(key))



class UrlSlugOperationService:

	@staticmethod
	def generateSlug(key):
		shurl_slug = UrlSlugService.generateSlug(key)
		return shurl_slug

	@staticmethod
	def getSlugUrl(slug):
		return UrlSlugService.basedecoder(slug)



