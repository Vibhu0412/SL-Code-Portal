
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('redeem/', views.redeem, name="redeem"),
    path('add_coupon/', views.add_coupon, name="add_coupon"),
]
