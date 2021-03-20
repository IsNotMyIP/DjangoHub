from django.urls import path

from . import views
app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('smoke/', views.toSmoke, name='smoke'),
    path('cigar/', views.cigars, name='cigars'),
    path('cigar/delete', views.delete, name='delete'),
]
