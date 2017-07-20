from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),  # Consolidated into 1 route
    url(r'^([0-9]{1,2})?$', views.index)
]
