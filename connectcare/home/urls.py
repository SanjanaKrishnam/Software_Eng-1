from django.conf.urls import url, include
from django.contrib import admin
from .views import main,doc,auth,doct


urlpatterns = [
   url(r'^$', main),
   url(r'docprof$',doc),
   url(r'auth$',auth),
   url(r'docts$',doct)
]
