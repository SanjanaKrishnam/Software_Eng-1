
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from uploads import views
from django_private_chat import urls as django_private_chat_urls




urlpatterns = [
        url(r'^', include('django_private_chat.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^',include('mysite.urls')),
    url(r'^home/',include('home.urls')),
    url(r'^profile/',include('profiledet.urls')),
    url(r'^test/',include('testres.urls')),
    url(r'^view/$',views.home),
    url(r'^view/uploads/$',views.upl),
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name': '../templates/registration/logout.html'}, name='logout'),
    url(r'^forum/',include('forum.urls')),
    url(r'^presc/',include('presc.urls')),
    url(r'^schedule/', include('scheduler.urls')),
             ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
