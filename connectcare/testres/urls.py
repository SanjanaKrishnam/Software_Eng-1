from django.conf.urls import url, include
from django.contrib import admin

from .views import main, testup

urlpatterns =[
url(r'^$',main),
url(r'^testup',testup),
]
