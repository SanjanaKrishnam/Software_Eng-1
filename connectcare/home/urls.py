from django.conf.urls import url, include
from django.contrib import admin
from .views import main,doc
urlpatterns = [
   url(r'^$', main),
   url(r'docprof$',doc),
]
