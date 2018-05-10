from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^mysite/', include('mysite.urls', namespace='mysite')),
    url(r'^admin/', include(admin.site.urls)),
]
