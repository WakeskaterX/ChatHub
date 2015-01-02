from django.conf.urls import patterns, include, url
from django.contrib import admin
from ChatHub.views import *


urlpatterns = patterns('ChatHub.views',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^msg/(\d+)[/]?$',router,{'GET':message_get}),
	url(r'^msg[/]?$',router,{'GET':new_message,'POST':message_post}),
)
