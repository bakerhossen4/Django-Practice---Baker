from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Courses( request ):
    return HttpResponse('Hi ! You are in App1/courses Page')
def About( request ):
    return HttpResponse('Hi ! You are in App1/AboutPage')
def Home( request ) :
    return HttpResponse(' This is App1 Page')
