from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='log_out'),
]
