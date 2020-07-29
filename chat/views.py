from django.shortcuts import render
from .forms import username
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    request.session[request.session.session_key]= request.POST.get('username')
    return render(request, 'chat/index.html')
    
# Create your views here.
def room(request, room_name,user_name):
    print(request.session.session_key)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user_name':user_name
        
    })
    
    # def access_session(request):
    # response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    # if request.session.get('name'):
    #     response += "Name : {0} <br>".format(request.session.get('name'))
    # if request.session.get('password'):
    #     response += "Password : {0} <br>".format(request.session.get('password'))
    #     return HttpResponse(response)
    # else:
    #     return redirect('create/')

