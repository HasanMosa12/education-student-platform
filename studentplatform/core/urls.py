from django.contrib import admin
from django.urls import path ,include
from .views import *
urlpatterns = [
    path('',homepage , name='homepage'),
    path('signupstudent',SignupStudent.as_view() , name='signupstudent'),
    path('signupparent',SignupParent.as_view() , name='signupparent'),
    path('signuplecturer',SignupLecturer.as_view() , name='signupLecturer'),
    path('loginstudent',loginstudent, name='loginstudent'),

]