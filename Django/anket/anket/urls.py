from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uygulama.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
from uygulama import views
urlpatterns=patterns('',
                     url(r'^polls/', include('uygulama.urls', namespace='uygulama')),
                     url(r'^admin/', include(admin.site.urls)),

    )