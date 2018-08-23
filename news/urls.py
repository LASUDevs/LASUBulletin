from django.urls import path,include
from . import views


urlpatterns = [
    path('create/', views.create_news, name='create_news'),
    path('<slug>/', views.news_detail, name='details')
]
