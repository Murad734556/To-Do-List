from django.urls import path
from .views import TaskList, task_create, task_update, task_delete
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from users.views import register, user_login, profile

urlpatterns = [
    path('', TaskList, name = 'tasks'),
    path('task/create/', task_create, name = 'task_create'),
    path('task/update/<int:id>', task_update, name = 'task_update'),
    path('task/delete/<int:id>', task_delete, name = 'task_delete'),
    path('register/', register, name = "register"),
    path('login/', user_login, name = "login"),
    path('user/<int:id>', profile, name = "profile"),
    path('logout/', LogoutView.as_view(next_page = 'tasks'), name = "logout"),
]