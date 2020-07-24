from django.shortcuts import render, redirect, HttpResponse
from home.models import User
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    password = request.POST['password']
    myhash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        username = request.POST['username'],
        password = myhash
    )
    return redirect('/')