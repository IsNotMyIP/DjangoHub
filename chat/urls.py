from django.urls import path

from . import views
app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.execu, name='execu'),
    path('smoke/', views.toSmoke, name='execu')
]
