"""smart_scheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from scheduler.views import todo_list
from scheduler.views import completed_task
from scheduler.views import new_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo_list/', todo_list),
    path('todo_list/completed/', completed_task, name='completed-task'),
    path('todo_list/new_task/', new_task, name='new-task'),
]
