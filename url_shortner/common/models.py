from django.db import models
from common.utils import DatetimeUtil , UniqueElemUtil

# Create your models here.


class BaseModel(models.Model):
	created_at = models.IntegerField(null = False,blank = False)
	updated_at = models.IntegerField(null = False,blank = False)
	deleted_at = models.IntegerField(null = True,blank = True)
	id_key = models.CharField(max_length=50,blank=False,null=False,unique=True)

	class Meta:
		db_table = 'common_tab'
		indexes = [models.Index(fields = [id_key])]

	def save(*args,**kwargs):
		self.updated_at = DatetimeUtil.unixtime()
		if not created_at:
			self.created_at = DatetimeUtil.unixtime()
		if not id_key:
			self.id_key = UniqueElemUtil.uniid_key(self.created_at,self.id)
		super(BaseModel,self).save(*args,**kwargs)
