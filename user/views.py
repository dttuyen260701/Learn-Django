from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def user(request):
    context = {'user':request.user}
    return render(request,  'user/user.html', context)

def profile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    return render(request,  'user/user.html', context)