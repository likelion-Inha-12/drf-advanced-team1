from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.create_assignment),
    path('submission/<int:pk>', views.create_submission)
]