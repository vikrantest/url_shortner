from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shortner_utils.validators import URLValidator
from shortner_app.shortnerservice import urlShortnerService

class ShortnerAPI(APIView):
	"""
	API for shortening URL
	"""

	def requestValidate(self,url):
		if not URLValidator.validateUrl(url):
			return False
		return URLValidator.getFragUrl(url)
		

	def post(self,request):
		request_data = request.data
		request_shurl = request_data['shurl_url']
		validated_data = self.requestValidate(request_shurl)
		shortner_service = urlShortnerService()

		if validated_data:
			print(validated_data)
			shortner_service = urlShortnerService()
			response = shortner_service(validated_data)
		else:
			return Response({'error':'Invalid Url'},status=status.HTTP_400_BAD_REQUEST)

		return Response({'response':'asfasdfa'},status=status.HTTP_201_CREATED)

	def get(self,request):
		return Response({'response':'asfasdfa'},status=status.HTTP_200_OK)
