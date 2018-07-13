import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shortner_utils.validators import URLValidator
from shortner_app.shortnerservice import urlShortnerDBService
from shortner_app.tasks import temp

logger = logging.getLogger(__name__)


class ShortnerAPI(APIView):
	"""
	API for shortening URL
	"""

	def requestmandateValidation(self,request_data):
		return URLValidator.mandatoryValidation(request_data)

	def requestUrlValidate(self,url):
		if not URLValidator.validateUrl(url):
			return False
		return URLValidator.getFragUrl(url)
		

	def post(self,request):
		request_data = request.data
		request_shurl = request_data.get('shurl_url','')
		if self.requestmandateValidation(request_data):
			validated_data = self.requestUrlValidate(request_shurl)
		else:
			return Response({'error':'Invalid Request'},status=status.HTTP_400_BAD_REQUEST)

		if validated_data:
			if request_data.get('new_shurl') and request_data['new_shurl'] in ['true',True]:
				validated_data['new_shurl'] = True
			else:
				validated_data['new_shurl'] = False
			shortner_service = urlShortnerDBService()
			response , exists = shortner_service(validated_data)
			if not exists:
				return Response({'shurl_slug':response},status=status.HTTP_201_CREATED)
			else:
				return Response({'shurl_slug':response},status=status.HTTP_200_OK)
		else:
			return Response({'error':'Invalid Url'},status=status.HTTP_400_BAD_REQUEST)

	def get(self,request):
		return HttpResponseRedirect({'response':'response'},status=status.HTTP_200_OK)



class ShortUrlConsumer(APIView):
	"""
	Short url consumer for redirection
	"""

	def get(self,request,shurl_slug):
		print(shurl_slug)
		shurl_slug = shurl_slug.strip()
		shortner_service = urlShortnerDBService()
		redirect_url = shortner_service(shurl_slug)
		print(redirect_url)
		logger.error(redirect_url)
		return HttpResponseRedirect(redirect_url)
