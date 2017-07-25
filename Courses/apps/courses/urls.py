from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.addcourse),
    url(r'^courses/destroy/(?P<id>\d+)$', views.delcourse),
    url(r'^delcourse2$', views.delcourse2)
]
