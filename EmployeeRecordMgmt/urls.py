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
from time_tracker.views import time_tracker, save_time_data_view, show_time_data
#from employee.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskReorder
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
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
    path('teammemhome/', views.TeamMemHome, name='teammemhome'),
    
    path('projectcreate/', views.CreateProject, name='projectcreate'),
    path('projectlist/', views.ProjectList, name='projectlist'),
    path('adminproject/', views.AdminProject, name='adminproject'),
    path('memtasklist/', views.MemTaskList, name='memtasklist'),
    path('addUser/', views.addUser, name='addUser'),
    path('teammemlogin/', views.TeamMemLogin, name='teammemlogin'),
    path('teammemregister/', views.TeamMemRegister, name='teammemregister'),
    #path('projectdetail<int:id>/',ProjectDetail.as_view(), name='projdetail'),
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
    
    path('time-tracker/', time_tracker, name='time_tracker'),
    path('save-data/', save_time_data_view, name='save_data'),
    path('time-data/', show_time_data, name='time_data'),
    
    path('delete/',views.DeleteTaskData, name='deleteTaskData'),
    path('tasklist/',views.TaskPage, name='tasklist'),
    path('',views.UpdateTaskData, name='updateTaskData'),
    path('addTaskData/',views.AddTask, name='addTaskData'),
#     path('home',home,name=home)
    # CREATE PROJECT
    #path('', TaskList.as_view(), name='tasks'),
    #path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    #path('task-create/', TaskCreate.as_view(), name='task-create'),
    #path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    #path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    #path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    #path('', include('base.urls')),
    
] 

admin.site.index_title = "DjangoNauts"
admin.site.site_header = "DjangoNauts Admin"
