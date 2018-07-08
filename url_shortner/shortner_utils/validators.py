import sys
import os
import re


class URLValidator:

	URL_REGEX = r"((http\://|https\://|ftp\://)|(www.))+(([a-zA-Z0-9\.-]+\.[a-zA-Z]{2,4})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(/[a-zA-Z0-9%:/-_\?\.'~]*)?"
	PREFIX_REGEX = r"(http\://|https\://|ftp\://)|(www.)"
	MANDATE_FIELDS = set(['new_shurl','shurl_url'])


	def validateUrl(url):
		valid = re.match(URLValidator.URL_REGEX,url)
		return valid

	def getFragUrl(url):

		prefix_data = "".join(re.split(r"^(www.)",url)[:-1])

		frag_url = re.sub(URLValidator.PREFIX_REGEX,'',url)

		return {'prefix_data':prefix_data,'frag_url':frag_url}

	def mandatoryValidation(dataset):
		data_keys = set(dataset.keys())
		inter_set = URLValidator.MANDATE_FIELDS - data_keys
		if URLValidator.MANDATE_FIELDS.__len__() != data_keys.__len__():
			return False
		else:
			inter_set = URLValidator.MANDATE_FIELDS - data_keys
			if inter_set.__len__()>0:
				return False

		return True