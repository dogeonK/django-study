from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_view),
    path('<str:topic>/', views.news_view, name='topic-page'),
    path('page/<int:num_page>/', views.num_page_view),
]
