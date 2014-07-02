from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^woyaolv/', include('woyaolv.urls')),
    
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/yangpo/work/python/woyaolv/mysite/static/css'}),
	(r'^script/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/yangpo/work/python/woyaolv/mysite/static/script'}),
	(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/yangpo/work/python/woyaolv/mysite/static/images'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)
