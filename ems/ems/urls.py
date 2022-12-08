"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include 
from admin_side.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('employee-list', employee_list, name="employee_list"),
    path('employee-edit/<int:pid>', edit_employee, name="edit_employee"),
    path('delete_employee/<int:pid>', delete_employee, name="delete_employee"),
    path('leave-status/<int:pid>', leave_status, name="leave_status"),
    path('admin_login',admin_login,name='admin_login'),
    path('admin_dashboard',admin_dashboard,name='admin_dashboard'),
    path('logout/',Logout),
    path('registration/',registration,),
    path('emp_login/',emp_login),
    path('emp_dashboard',emp_dashboard,name='emp_dashboard'),
    path('emp_profile/',profile, ),
    path('change_password',change_password,name='change_password'),

]
