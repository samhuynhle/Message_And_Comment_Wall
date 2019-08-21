from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^wall/(?P<user_id>[0-9]+)$', views.wall),
    url(r'^postmessage$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^delete_comment$', views.delete_comment),
    url(r'^delete_message$', views.delete_message),
]