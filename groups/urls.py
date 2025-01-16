from django.urls import path
from . import views


app_name = 'groups'

urlpatterns = [
    path('list', views.group_list, name='group_list'),
    path('create', views.group_create, name='create'),
    path('update/<int:pk>/', views.group_update, name='update'),
    path('detail/<int:pk>/', views.group_detail, name='detail'),
    path('delete/<int:pk>/', views.group_delete, name='delete')
]