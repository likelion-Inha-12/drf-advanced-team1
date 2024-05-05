from django.contrib import admin
from django.urls import path
from . import views

# drf_project/urls.py 에다가 assignment/로 연결시켜놔서 postman에서 사용하실때 "assignment/" 써주신 다음에 여기 url 쓰시면 될거같아요!
urlpatterns = [
    path('post/', views.create_assignment),
    path('submission/<int:pk>', views.create_submission)
]
