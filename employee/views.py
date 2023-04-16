from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project,Employees,Profile, Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from .forms import EmployeeRegistration,profileForm,CreteUserForm,ProjectCrete, TaskCreate

#from django.contrib.auth.forms import UserCreationForm
#from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
#from .models import Task
#from django.urls import reverse_lazy
#from django.views import View
#from django.shortcuts import redirect
#from django.db import transaction

#from employee.models import Task
#from employee.forms import PositionForm


# Create your views here.
#This fun add emp
def AddEmp(request):
    if request.method == 'POST':
      fm = EmployeeRegistration(request.POST)
      if fm.is_valid():
          eid=fm.cleaned_data['empid']
          nm=fm.cleaned_data['name']
          jb=fm.cleaned_data['job']
          em=fm.cleaned_data['email']
          ph=fm.cleaned_data['phone']
          reg=Employees(empid=eid,name=nm,job=jb,email=em,phone=ph)
          reg.save()
          fm = EmployeeRegistration()
          return redirect('employees')
    else:
      fm = EmployeeRegistration()
   
    return render(request, 'AddEmp.html',{'form':fm})


def AddTask(request):
    if request.method == 'POST':
        fm = TaskCreate(request.POST)
        if fm.is_valid():
            pt = fm.cleaned_data['ptitle']
            nm = fm.cleaned_data['name']
            reg = Task(ptitle=pt,name=nm)
            reg.save()
            fm = TaskCreate()
            return redirect('tasklist')
    else:
            
        fm = TaskCreate()
            
    return render(request, 'addTaskData.html',{'form':fm})


def CreateProject(request):
    if request.method == 'POST':
       fm=ProjectCrete(request.POST)
       if fm.is_valid():
          pt=fm.cleaned_data['ptitle']
          pd=fm.cleaned_data['pdesc']
          
          reg=Project(ptitle=pt,pdesc=pd)
          reg.save()
          fm = ProjectCrete()
          return redirect('teamheadhome')
    else:
        fm=ProjectCrete() 
    return render(request, 'project_create_form.html',{'form':fm})

def TaskPage(request):
    if request.method == 'POST':
        fm = TaskCreate(request.POST)
        
    else:
        fm = TaskCreate()
    task = Task.objects.all()
    return render(request, 'tasklist.html',{'form':fm,'ts':task})

#This fun show data
def EmpPage(request):
    if request.method == 'POST':
      fm = CreteUserForm(request.POST)
      
    else:
      fm = CreteUserForm()
    employee = Profile.objects.all()

    return render(request, 'employees.html',{'form':fm,'em':employee})

#This fun will delete data
def DeleteData(request,id):
    if request.method=='POST':
        pi = Employees.objects.get(pk=id) 
        pi.delete()
        return redirect('employees')
    

def DeleteTaskData(request, t_id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=t_id)
        pi.delete()
        return redirect('tasklist')

#This fun will update data
def UpdateEmp(request,id):
 if request.method == 'POST':
    pi=Employees.objects.get(pk=id)
    fm=EmployeeRegistration(request.POST,instance=pi)
    
    if fm.is_valid():
     fm.save()
     return redirect('employees')
 else:
      pi=Employees.objects.get(pk=id)
      fm=EmployeeRegistration(instance=pi)
      
 return render(request, 'updateEmp.html',{'form':fm})


def UpdateTaskData(request, t_id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=t_id)
        fm = TaskCreate(request.POST, instance=pi)
        
        if fm.is_valid():
            fm.save()
            return redirect('tasklist')
    else:
        pi = Task.objects.get(pk=t_id)
        fm = TaskCreate(instance=pi)
    return render(request, 'updateTaskData.html',{'form':fm})



def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('adminhome')
        elif not username or not pass1:
            messages.success(request, 'Both Username and Password are required.')
            return redirect('login')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return render(request, 'logout.html')

def TeamHeadLogout(request):
    logout(request)
    return render(request, 'teamheadlogout.html')

def admin(request):
    return render(request,'admin.html')

def ForgotPass(request):    
    return render(request, 'forgotpass.html')

def AdminHomePage(request):
    context = {
        #'page_title':'Home',
       # 'employees':employees,
        
        'total_project':len(Project.objects.all()),
        'total_employee':len(Employees.objects.all()),
    }
    return render(request, 'adminhome.html',context)

def TeamHeadRegister(request):
    form = CreteUserForm()
    
    if request.method == 'POST':
        form = CreteUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            
            return redirect('teamheadlogin')
    
    context = {'form':form}
    return render(request, 'teamheadregister.html', context)


def TeamHeadLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('teamheadhome')
        else:
            messages.info(request, 'Username or Password is incorrect')
        
    context = {}
    return render(request, 'teamheadlogin.html', context)

def TeamHeadHome(request):
    context = {
        #'page_title':'Home',
       # 'employees':employees,
       
        'total_project':len(Project.objects.all()),
        'total_employee':len(Employees.objects.all()),
    }
    return render(request, 'teamheadhome.html',context)

def TeamMemHome(request):
    return render(request, 'teammemhome.html')

def ProjectList(request):
     context = {
        #'page_title':'Home',
       # 'employees':employees,
       'projects':Project.objects.all(),
       
     }
     return render(request, 'projectlist.html',context)

def AdminProject(request):
     context = {
        #'page_title':'Home',
       # 'employees':employees,
       'projects':Project.objects.all(),
       
     }
     return render(request, 'adminproject.html',context)

def MemTaskList(request):
    if request.method == 'POST':
        fm = TaskCreate(request.POST)
        
    else:
        fm = TaskCreate()
    task = Task.objects.all()
    return render(request, 'memtasklist.html',{'form':fm,'ts':task})
    

def TaskListabc(request):
    return render(request, 'todo.html')

def ProList(request):
    return render(request, 'task_list.html')


def addUser(request):
    if request.method == 'POST':
        form = CreteUserForm(request.POST)
        profile_form = profileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            #we don't save the profile_form here because we have to first get the value of profile_form, assign the user to the OneToOneField created in models before we now save the profile_form. 

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            messages.success(request,  'Your account has been successfully created')

            return redirect('employees')
    else:
        form = CreteUserForm()
        profile_form = profileForm()
        
   
    return render(request, 'addUser.html', {'form': form, 'profile_form': profile_form})


def TeamMemLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('teammemhome')
        else:
            messages.info(request, 'Username or Password is incorrect')
        
    context = {}
    return render(request, 'teammemlogin.html', context)

def TeamMemRegister(request):
    form = CreteUserForm()
    
    if request.method == 'POST':
        form = CreteUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            
            return redirect('teammemlogin')
    
    context = {'form':form}
    return render(request, 'teammemregister.html', context)
