from django.urls import path
from board import views

urlpatterns = [
    path('', views.board),
    path('first/', views.boardfirst),   # 127.0.0.1/8000/boards/first

]