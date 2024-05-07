from django.contrib import admin
from django.urls import path
from . import views
from .views import AssignmentAPIView

# drf_project/urls.py 에다가 assignment/로 연결시켜놔서 postman에서 사용하실때 "assignment/" 써주신 다음에 여기 url 쓰시면 될거같아요!
urlpatterns = [
    path('post/', views.create_assignment),
    path('submission/<int:pk>/', views.create_submission),
    path('submission/list/', views.AssignmentListAPIView.as_view(), name='List'),
    path('submission/list/<int:pk>/', views.AssignmentAPIView.as_view(), name='Detail'),
    path('submission/update/<int:pk>/', views.update_assignment),
    path('submission/delete/<int:pk>/', views.AssignmentAPIView.as_view(), name='Delete'),
    path('part/<str:part>', views.get_part),
    path('tag/<str:tag>', views.get_tag),
]
