
from django.http import HttpResponse

def contact( ret ) :
    return HttpResponse("Hi ! Baker. This is Contact Page")

def home( request ) :
    return HttpResponse("This is Home Page") 