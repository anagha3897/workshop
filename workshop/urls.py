from django.conf.urls import url
from django.contrib import admin
from registration.views import Home
from registration import urls as reg_url
from django.conf.urls import include, url
urlpatterns = [
        url(r'^$', Home.as_view(), name='home'),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^registration/', include(reg_url)),
]
