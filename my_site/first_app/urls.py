from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_view),
    path('<topic>/', views.news_view),
]
