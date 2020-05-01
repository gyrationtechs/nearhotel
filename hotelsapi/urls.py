from django.contrib import admin
from hotelsapi import views


urlpatterns = [
    url(r'^cords/', views.test_geocode, name='cords'),
    url(r'^properties/', views.near_hotels, name='near_hotels'),
]