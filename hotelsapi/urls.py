from django.contrib import admin
from hotelsapi import views
from django.conf.urls import url


urlpatterns = [
    url(r'^cords/', views.test_geocode, name='cords'),
    url(r'^properties/', views.near_hotels, name='near_hotels'),
    #url(r'^properties/(?at=<lat>,<lng>\d{2,18})', views.places_result, name='places'),
]