from django.urls import path
from todo.views import TodoList, TodoCreate, TodoDetail, TodoUpdate, TodoDelete

urlpatterns = [
    path('', TodoList.as_view(), name='index'),
    path('new', TodoCreate.as_view(), name='new-todo'),
    path('<pk>', TodoDetail.as_view(), name='view-todo'),
    path('<pk>/edit', TodoUpdate.as_view(), name='edit-todo'),
    path('<pk>/delete', TodoDelete.as_view(), name='del-todo')
]
