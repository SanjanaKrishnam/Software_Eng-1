from django.conf.urls import url, include
from django.contrib import admin

from.views import main

urlpatterns =[
url(r'^$',main),

]
