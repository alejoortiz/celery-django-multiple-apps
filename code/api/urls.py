from django.urls import path
from api import views


urlpatterns = [
    path('main/', views.main, name='main'),
]
