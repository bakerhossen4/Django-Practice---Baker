from django.shortcuts import render
from django.http import HttpResponse

def Home( req ) :
    return HttpResponse(' This is App2 Page')
# Create your views here.
