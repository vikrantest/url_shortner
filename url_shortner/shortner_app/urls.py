from django.conf.urls import url
from django.contrib import admin
from shortner_app.views import *

urlpatterns = [
    url(r'^myshurl/generate-shurl/$', ShortnerAPI.as_view()),# chaeck / allowance
]
