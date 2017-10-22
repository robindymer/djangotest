from django.conf.urls import url, include
from django.contrib import admin
from notes.views import index

urlpatterns = [
    url(r'^index/', index, name="index"),
]
