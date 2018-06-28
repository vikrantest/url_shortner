from django.conf.urls import url
from django.contrib import admin
from shortner_app.views import *

urlpatterns = [
    url(r'^myshurl/generate-shurl/$', ShortnerAPI.as_view()),# chaeck / allowance
    url(r'^(?P<shurl_slug>[\w{}.-]{1,9})$', ShortUrlConsumer.as_view()),# chaeck / allowance(?P<obj_key>[\w{}.-]{1,32})$
]
