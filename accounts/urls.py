from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path("login/", LoginView.as_view(template_name="accounts/login.html"),name="user_login"),
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"),name="user_logout"),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('contact/', views.view_contact, name='contact'),
    path('program/', views.view_program, name='program'),
]