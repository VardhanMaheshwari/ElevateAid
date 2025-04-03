from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_view'),
    path('register/', views.register_page, name='register_view'),
    path('api/register/', views.api_user_register, name='api_user_register'),
    path('api/login/', views.api_user_login, name='api_user_login'),
    path('api/logout/', views.api_user_logout, name="api_user_logout"),
]