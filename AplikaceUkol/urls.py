from django.urls import path
from . import views

app_name = "AplikaceUkol"
urlpatterns = [
    path('', views.index, name='index'),
    path('engines/<int:pk>/', views.engine_detail, name='engine_detail'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('manufacturers/<int:pk>/', views.manufacturer_detail, name='manufacturer_detail'),
]