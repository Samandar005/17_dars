from django.urls import path
from . import views

app_name = 'teachers'


urlpatterns = [
    path('list/', views.teacher_list, name='teacher_list'),
    path('create/', views.teacher_create, name='teacher_create'),
    path('update/<int:pk>/', views.teacher_update, name='update'),
    path('detail/<int:pk>/', views.teacher_detail, name='detail'),
    path('delete/<int:pk>/', views.teacher_delete, name='delete')
]