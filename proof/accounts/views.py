
#django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.urls import reverse, reverse_lazy

#local
from .forms import UserProfileInfoForm, UserForm
from projects.models import Project, Task, TeamRecord
# Create your views here.

def register(request):
    if request.method == 'POST':
        #get data from request
        form = UserCreationForm(request.POST)
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # save user form
        user = user_form.save(commit=False)
        # first use first_name and last_name to create nickname
        username='{}{}'.format(first_name, last_name)
        user.username = username
        user.password = 'testpassword'
        user.email = user.email.lower()
        #check if new user does not duplicate either username nor email
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html',{
            'messages':'User with the same First and Last Name already exists in database. You can not duplicate user.',
            'user_form':user_form,
            'profile_form':profile_form})
        if User.objects.filter(email=user.email).exists():
            return render(request, 'accounts/register.html',{
            'messages':'User with the same email already exists in database. Email have to be unique.',
            'user_form':user_form,
            'profile_form':profile_form})

        user.set_password(user.password)
        user.save()

        #save user profile form
        profile = profile_form.save(commit=False)
        profile.user = user

        #check if profile picture is ready to be saved
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
            profile.save()
        else:
            print(user_form.errors, profile_form.errors)

        messages = 'New User: {} was created.'.format(user.username)
        return render(request, 'accounts/login.html',{'messages':messages})
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        return render(request, 'accounts/register.html',{'user_form':user_form,
                                        'profile_form':profile_form})


def user_login(request):
    if request.method == 'POST':
        #print('login details are analyst')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            username = get_object_or_404(User, email=email).username
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    # log in with passwod
                    login(request, user)
                    messages = 'You are logged in as: {}.'.format(user.username)
                    return redirect('accounts:profile')
                else:
                    #user not active
                    return render(request, 'accounts/login.html',{'messages':'User is not active.'})
            else:
                # wrong password or username
                return render(request, 'accounts/login.html',{'messages':'invalid login details.'})
        else:
            return render(request, 'accounts/login.html',{'messages':'Email does NOT exists in database.'})
    else:
        # GET
        return render(request, 'accounts/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

@login_required
def profile(request):
    if request.user.is_authenticated():
        # GENERTE CONTEXT DATA FOR STAFF AND NORAL USERS
        tasks = Task.objects.filter(master=request.user)
        #Get user projects and remove duplicates
        my_projects = TeamRecord.objects.filter(member=request.user).distinct()
        project_list = []
        if my_projects.count() >=1:
            for i in my_projects:
                append_flag = True
                for item in project_list:
                    if i.project.id == item.id:
                        append_flag = False
                if append_flag==True:
                    project_list.append(i.project)
            my_projects = project_list

        # GENERATE ADDITIONAL DATA FOR STAFF
        if request.user.is_staff:
            #generate context data for staff member
            all_users = User.objects.all()
            all_projects = Project.objects.all()
            context = {'user':request.user, 'tasks':tasks, 'my_projects':my_projects,'all_users': all_users, 'all_projects':all_projects}
        else:
            #generate context data for NON staff member

            context = {'user':request.user, 'tasks':tasks, 'my_projects':my_projects}

        return render(request,'accounts/profile.html',context)

    else:
        return redirect('accounts:login')
