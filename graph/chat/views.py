from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', locals())

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


def canvas(request):
    return render(request, 'chat/canvas.html', locals())

def snake(request):
    return render(request, 'chat/snake.html', locals())