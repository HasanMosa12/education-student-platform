from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate , login
# Create your views here.


class SignupStudent(CreateView):
    model = User
    form_class = SignupStudent
    template_name = 'signupstudent.html'


    def form_valid(self,form):
        user = form.save()
        return redirect('homepage')
class SignupLecturer(CreateView):
    model = User
    form_class = SignupLecturer
    template_name = 'signuplecturer.html'


    def form_valid(self,form):
        user = form.save()
        return redirect('homepage')
class SignupParent(CreateView):
        model = User
        form_class = SignupParent
        template_name = 'signupparent.html'

        def form_valid(self, form):
            user = form.save()
            return redirect('homepage')


def loginstudent(request):
    if request.method == "GET" :
        return render(request,'loginstudent.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            print("wrong username or password")
            return redirect('loginstudent')



def homepage(request):
    return render(request , 'homepage.html')