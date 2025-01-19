from django.urls import path
from . import views
from .views_manage import manage_booking

urlpatterns = [
    path("make/", views.make_booking, name="make_booking"),
    path("manage/", manage_booking, name="manage_booking"),
]
