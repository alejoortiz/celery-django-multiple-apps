from django.urls import path
from web import views


urlpatterns = [
    path('main/', views.main, name='main'),
]
