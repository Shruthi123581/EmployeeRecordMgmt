from django.contrib import admin
#from .models import Task
# from django.contrib.admin import AdminSite
# from django.contrib.auth.models import Group, User


# # Register your models here.

from .models import Employees,Project,Profile, Task

@admin.register(Employees)
class EmpAdmin(admin.ModelAdmin):
    list_display = ('empid','name','job','email','phone')
# from myadmin import my_admin_site
@admin.register(Project)
class EmpAdmin(admin.ModelAdmin):
    list_display = ('ptitle','pdesc')

@admin.register(Profile)
class ProAdmin(admin.ModelAdmin):
    list_display = ('user','name','email','address')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('ptitle', 'name')

# my_admin_site.register(MyModel)

'''

admin.site.register(Task)
'''