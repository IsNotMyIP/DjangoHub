from django.urls import path

from . import views
app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='test'),
    path('smoke/', views.toSmoke, name='smoke'),
    path('cigar/', views.cigars, name='cigars'),
    path('login/', views.login, name='chat_login'),
]
