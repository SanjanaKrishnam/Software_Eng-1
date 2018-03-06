from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from .views import CreateMyModelView


urlpatterns =[
url(r'^$',CreateMyModelView.as_view()),

]
