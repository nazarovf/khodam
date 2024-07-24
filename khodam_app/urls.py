from django.urls import path
from .views import generate_khodam

urlpatterns = [
    path('', generate_khodam, name='generate_khodam'),
]
