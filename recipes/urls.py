from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('<int:user_id>/', my_recipes, name="my_recipes"),
    path('all_recipes/', all_recipes, name='all_recipes'),
    path('create/', views.create_post, name='create_post'),
    path('<int:pk>/update/', views.update_post, name='recipes-update'),
    path('<int:pk>', RecipeDetailView.as_view(), name="recipes-detail"),
    path('<int:pk>/delete', views.delete_post, name="recipes-delete"),
]
