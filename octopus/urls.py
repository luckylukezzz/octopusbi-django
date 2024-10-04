from django.urls import path
from . import views

urlpatterns = [
     path('', views.dashboard, name='dashboard'),
    path('table/<str:table_name>/', views.table_view, name='table_view'),
]