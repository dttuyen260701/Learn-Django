
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from room.models import Topic

# Create your views here.
def home(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request,  'home/home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def loginPage(request):
    page = 'login'
    if(request.user.is_authenticated):
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username OR Password does not exist')
    context = {'page':page}
    return render(request,  'user/login_register.html', context)

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Error')
    return render(request,  'user/login_register.html', {'form':form})