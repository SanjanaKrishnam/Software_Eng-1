
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls import include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('mysite.urls')),
     url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name': '../templates/registration/logout.html'}, name='logout'),
]
