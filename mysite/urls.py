from django.conf.urls import patterns, include, url
from woyaolv.views import woyaolv,planfix,wanttravel,paris,seeproposetraveler,fromairport,toairport
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^woyaolv/$',woyaolv),
    url(r'^woyaolv/planfix/$',planfix),
    url(r'^woyaolv/seeproposetraveler/$',seeproposetraveler),
    url(r'^woyaolv/wanttravel/$',wanttravel),
    url(r'^woyaolv/fromairport/$',fromairport),
    url(r'^woyaolv/toairport/$',toairport),
    url(r'^woyaolv/planfix/paris/$',paris),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/sli/coding/python/djcode/mysite/mysite/static/css'}),
	(r'^script/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/sli/coding/python/djcode/mysite/mysite/static/script'}),
	(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/sli/coding/python/djcode/mysite/mysite/static/images'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)
