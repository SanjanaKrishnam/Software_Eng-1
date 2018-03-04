from django.conf.urls import url, include
from django.contrib import admin
from .views import upload
urlpatterns = [
    url(r'^$', upload),

]
