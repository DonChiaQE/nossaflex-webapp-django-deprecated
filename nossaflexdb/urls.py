from django.urls import path
from . import views

urlpatterns = [
    path('', views.database),
    path('login/', views.login),
    path('signup/', views.signup),
    path('database/', views.database),
]