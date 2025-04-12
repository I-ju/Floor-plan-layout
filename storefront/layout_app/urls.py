from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/furnitures/', views.get_furnitures, name='get_furnitures'),
    path('api/save_furniture/', views.save_furniture, name='save_furniture'),
    path('api/reset_layout/', views.reset_layout, name='reset_layout'),
]