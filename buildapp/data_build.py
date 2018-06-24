#! /usr/bin/python
import os
import sys

import django
from django.core.wsgi import get_wsgi_application
sys.path.insert(0, '/Users/vikrant/vikrant/workspace/vikrant/tala/bankproj/bankproj')
sys.path.append('/Users/vikrant/vikrant/workspace/vikrant/tala/bankproj/bankproj/bankproj')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bankproj.settings'
application = get_wsgi_application()

from bankapp.models import AccountRules,BankCurrency,BankAccountProfile,BankAccount

class ProjectTestDataSet:

	def __init__(self):
		self.account_request_data = {'first_name':'vikrant','last_name':'singh','date_of_birth':651024128,'gender':'male','address':'bangalore','pincode':'560076',
								'account_id_num':'DULPS1990V','account_number':'HSBC100023456','ifsc_code':'HSBC1000'}
		self.currency_request_data = {'currency_name':'dollar','currency_symbol':'$'}
		self.account_rules_data = {'max_deposit_per_transaction':60,'max_deposit_per_day_frequency':4,'max_deposit_per_day':160,
						'min_withdrawl_per_transaction':20,'min_withdrawl_per_day_frequency':3,'min_withdrawl_per_day':50}

	def setup(self):
		BankCurrency.objects.all().delete()
		AccountRules.objects.all().delete()
		BankAccountProfile.objects.all().delete()
		BankAccount.objects.all().delete()
		currency_obj = BankCurrency.objects.create(currency_name=self.currency_request_data['currency_name'],currency_symbol=self.currency_request_data['currency_symbol'])
		account_rules_obj = AccountRules.objects.create(max_deposit_per_transaction=self.account_rules_data['max_deposit_per_transaction'],
							max_deposit_per_day_frequency=self.account_rules_data['max_deposit_per_day_frequency'],
							max_deposit_per_day=self.account_rules_data['max_deposit_per_day'],
							min_withdrawl_per_transaction=self.account_rules_data['min_withdrawl_per_transaction'],
							min_withdrawl_per_day_frequency=self.account_rules_data['min_withdrawl_per_day_frequency'],
							min_withdrawl_per_day=self.account_rules_data['min_withdrawl_per_day'])
		account_profile_obj = BankAccountProfile.objects.create(first_name=self.account_request_data['first_name'],last_name=self.account_request_data['last_name'],
						date_of_birth=self.account_request_data['date_of_birth'],gender=self.account_request_data['gender'],pincode=self.account_request_data['pincode'],
						address=self.account_request_data['address'],account_id_num=self.account_request_data['account_id_num'])
		account_obj = BankAccount.objects.create(account_profile=account_profile_obj,account_number=self.account_request_data['account_number'],
						account_rules=account_rules_obj,account_ifsc=self.account_request_data['ifsc_code'],account_currency=currency_obj)

if __name__ == '__main__':
	ProjectTestDataSet().setup()

db.seqcounter.insert({_id:"seqid",sequence_val:100})
