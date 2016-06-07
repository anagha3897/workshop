from django.contrib import admin
from registration.views import Home
from registration import urls as reg_urls
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^registration/', include(reg_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
