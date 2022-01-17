from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import MessagesArea


def index(request):
    return render(request, "index.html")


def signupHandle(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if (username or email or password) == "":
            messages.error(request, "username, email, password Should Not EMPTY.!")
            return redirect('index')
        elif not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('../')
        elif User.objects.filter(username=username).exists():
            messages.error(request, "This name already taken try with Your nick name please.")
            return redirect("../")

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Your RChat Account created SuccessFully.!  ")
            return redirect("../")
        return redirect('../')

    else:
        return HttpResponse("404 Not Found")


def loginHandle(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully locked IN..")
            return redirect("../")

        else:
            messages.error(request, 'Credential Error Please try again..')
            return redirect('../')


def logoutHandle(request):
    logout(request)
    messages.success(request, "Successfully LogOut..")
    return redirect("../")


def submit(request):
    if request.method == 'POST':
        mesage = request.POST.get('text')
        if mesage == "":
            messages.error(request, "Massege should not empty")
            return redirect("../")
        obj = MessagesArea.objects.create(user=request.user, message=mesage)
        return JsonResponse({
            'status': True,
            'message': obj.message,
            'timeStamp': obj.timeStamp
        })

    return JsonResponse({
        'status': False,
        'message': 'Invalid request'
    })
