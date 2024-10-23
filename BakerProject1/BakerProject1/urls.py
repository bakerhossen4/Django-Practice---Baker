
from django.contrib import admin
from django.urls import path, include
#from views import contact
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact),
    path('', views.home),
    path('app1/',include("BakerApp1.urls")),
    path('app2/',include("BakerApp2.urls"))
]
