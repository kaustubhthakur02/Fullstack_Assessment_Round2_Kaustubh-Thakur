from django.urls import path
from .import views

urlpatterns = [
    path('', views.login_page, name='login_page'),  
    path('authenticate/', views.authenticate_user, name='authenticate_user'),
]