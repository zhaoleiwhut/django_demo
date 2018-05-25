from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_list/', views.get_list, name='get_list'),
    path('save/', views.save, name='save'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
