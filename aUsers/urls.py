from django.contrib import admin
from django.urls import path
from . import views
app_name = 'aUsers'
urlpatterns = [
    path('', views.welcome),
    path('register/', views.register),
    path('login/', views.login, name ="logito"),
    path('logout/', views.logout),

]