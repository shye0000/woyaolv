from django.conf.urls import patterns, url
from woyaolv.views import woyaolv,planfix,wanttravel,paris,seeproposetraveler,fromairport,toairport

urlpatterns = patterns('',

	url(r'^$',woyaolv),
    url(r'^planfix/$',planfix),
    url(r'^seeproposetraveler/$',seeproposetraveler),
    url(r'^wanttravel/$',wanttravel),
    url(r'^fromairport/$',fromairport),
    url(r'^toairport/$',toairport),
    url(r'^planfix/paris/$',paris),
    )