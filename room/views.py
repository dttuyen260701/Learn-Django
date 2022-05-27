from django.db.models import CharField
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse
from .roomform import RoomForm
from django.contrib.auth.decorators import login_required
# Create your views here.
#rooms = Room.objects.all()
def room(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,  'room/room.html', context)

def detail(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user= request.user,
            room = room,
            body =request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room:detail', pk = room.id)
    context = {'room':room, 'messages':room_messages, 'participants':participants}
    return render(request,  'room/roomdetail.html', context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'room/roomform.html', context)

@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'room/roomform.html', context)

@login_required(login_url='/login')
def delRoom(request, pk):
    room = Room.objects.get(id=pk)
    context = {'obj':room}

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
    if request.method == 'POST':
        room.delete()
        return redirect('/')
    return render(request, 'room/delroom.html', context)

@login_required(login_url='/login')
def delCMT(request, pk):
    mess = Message.objects.get(id=pk)
    context = {'obj ':mess}

    if request.user != mess.user:
        return HttpResponse('You are not allowed here!!')
    if request.method == 'POST':
        mess.delete()
        return redirect('/')
    return render(request, 'room/delroom.html', context)

def topicRoom(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(descreption__icontains=q)
    )
    context = {'rooms':rooms}
    return render(request,  'room/room.html', context)