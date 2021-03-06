from django.urls import path

from mng import views


app_name = 'mng'

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('add', views.add, name='add'),
    path('all_tasks', views.all_tasks, name='all_tasks'),
    path('edit/<int:task_id>', views.task_edit, name='task_edit'),
    path('edit/<int:task_id>/add_progress', views.add_progress, name='add_progress'),
    path('testing', views.testing, name='test'),
]