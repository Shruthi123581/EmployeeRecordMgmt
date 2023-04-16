"""EmployeeRecordMgmt URL Configuration

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
from employee import views
from django.contrib.auth import views as auth_views
#from employee.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskReorder
from time_tracker.views import time_tracker, save_time_data_view, show_time_data


urlpatterns = [
    #path('', views.index, name='index'), 
    #path('all_events/', views.all_events, name='all_events'), 
    #path('add_event/', views.add_event, name='add_event'), 
    #path('update/', views.update, name='update'),
    #path('remove/', views.remove, name='remove'),
    
    path('admin/', admin.site.urls),
    path('forgotpass/', views.ForgotPass, name='forgotpass'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),

    path('delete/<int:id>/',views.DeleteData, name='deleteData'),
     path('employees/',views.EmpPage, name='employees'),
      path('<int:id>/',views.UpdateEmp, name='updateData'),
      path('addEmp/',views.AddEmp, name='addEmp'),
     # path('inactiveEmp/',views.InactiveEmp, name='inactiveEmp'),
      
    path('',views.HomePage, name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('teamheadlogout/',views.TeamHeadLogout,name='teamheadlogout'),
    #path('admin/', views.admin,name='admin'),
    path('adminhome/', views.AdminHomePage, name='adminhome'),
    path('teamheadregister/', views.TeamHeadRegister, name='teamheadregister'),
    path('teamheadlogin/', views.TeamHeadLogin, name='teamheadlogin'),
    path('teamheadhome/', views.TeamHeadHome, name='teamheadhome'),
    path('teammemlogin/', views.TeamMemLogin, name='teammemlogin'),
    path('addUser/', views.addUser, name='addUser'),
    path('teammemlogin/', views.TeamMemLogin, name='teammemlogin'),
    path('todo/', views.TaskListabc, name='todo'),
    #path('main/', views.Main, name='main'),
    path('task_list/', views.ProList, name='task_list'),
    
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
         name="reset_password"),
    
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
         name="password_reset_done"),
    
    path('reset/<uidb64>/<token>', 
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
         name="password_reset_confirm"),
    
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
         name="password_reset_complete"),
#     path('home',home,name=home)

    path('time-tracker/', time_tracker, name='time_tracker'),
    path('save-data/', save_time_data_view, name='save_data'),
    path('time-data/', show_time_data, name='time_data'),
    
    path('projectcreate/', views.CreateProject, name='projectcreate'),
    path('projectlist/', views.ProjectList, name='projectlist'),
    path('adminproject/', views.AdminProject, name='adminproject'),
    
    path('delete/<int:name>/',views.DeleteTask, name='deleteTask'),
    path('tasks/',views.TaskPage, name='tasks'),
    path('<int:name>/',views.UpdateTask, name='updateTask'),
    path('addTask/',views.AddTask, name='addTask'),

    
]

admin.site.index_title = "DjangoNauts"
admin.site.site_header = "DjangoNauts Admin"
