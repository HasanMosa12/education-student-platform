from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import *
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




def homepage(request):
    return render(request , 'homepage.html')