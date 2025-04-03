from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name="home_view"),
    # path('home/donor/', views.donor_home_view, name="donor_home_view"),
    # path('home/receiver/', views.receiver_home_view, name="receiver_home_view"),
]
