from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.staff_login, name='home'),  # Default page or staff login
    path('admin-login/', views.admin_login, name='admin_login'),  # Admin login page
    path('staff-login/', views.staff_login, name='staff_login'),  # Staff login page
    path('register/', views.register_view, name='register'),  # Registration page
    path('admin-dashboard/', views.dashboard_view, name='dashboard'),  # Admin dashboard page
    path('logout/', views.logout_view, name='logout'),  # Logout page
]
