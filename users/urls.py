from django.urls import path, include
from . import views
from .views import account

urlpatterns = [
    path('', account, name='account'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('logout', views.logout_user, name='logout'),
]
