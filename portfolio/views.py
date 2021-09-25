from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects



def home(request):
    projects=Projects.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects})


