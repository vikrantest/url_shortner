import time
import datetime
import os
import uuid
import re
import math
import string
from django.conf import settings as my_settings


class DatetimeUtil:

	@staticmethod
	def unixtime(datetime_obj = None):
		"""
		Get current epoch time or convert given datetime to epoch time
		"""
		if not datetime_obj:
			return int(time.time())
		else:
			return datetime_obj.strftime('%s')

	@staticmethod
	def local_datetime(unixtime):
		"""
		Get Local datetime object from epoch time
		"""
		return datetime.datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unixtime)),'%Y-%m-%d %H:%M:%S')

	@staticmethod
	def unix_datetime(unixtime):
		"""
		Get utc datetime obj from epoch time
		"""
		return datetime.datetime.fromtimestamp(unixtime)

	@staticmethod
	def day_start_end_unixtime(unixtime,local_time = False):
		"""
		get local day start and end hours
		"""
		datetime_obj = DatetimeUtil.get_local_datetime(unixtime) if local_time else DatetimeUtil.unix_datetime(unixtime)
		start_time = unixtime - ((datetime_obj.hour*60*60)+(datetime_obj.minute*60)+datetime_obj.second)
		end_time = start_time + (24*60*60)-1
		return start_time,end_time


class UniqueElemUtil:

	@staticmethod
	def uniid_key(base_id):
		param = DatetimeUtil.unixtime()
		p0 = str(param)[:4]
		p1 = ''.join(list(filter(str.isdigit,re.findall('..', '%012x' % uuid.getnode()))))
		p2 = str(base_id)
		p3 = str(param)[4:8]

		return p0+p2+p3


class UrlSlugService:

	mapper = string.ascii_lowercase+string.digits+string.ascii_uppercase
	base_val = my_settings.BASE_CONVERSION_VAL

	@classmethod
	def baseencoder(cls,key):
		slug = ''
		while key:
			slug = cls.mapper[key%cls.base_val]+slug
			key = math.floor(key/cls.base_val)
		return slug



	@classmethod
	def basedecoder(cls,slug):
		key = 0
		lent = len(slug)
		res = 0
		for m in range(lent):
			key = key * cls.base_val + cls.mapper.find(slug[m])
		return key
		

	@classmethod
	def generateSlug(cls,key):
		return cls.baseencoder(key)

	
