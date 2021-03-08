from django.urls import path

from . import views
app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('smoke/', views.toSmoke, name='smoke'),
    path('cigar/', views.cigars, name='cigars')
]
