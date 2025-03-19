from django.shortcuts import render, redirect
from service.models import help,Card
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def home(request):
    ServiceData = help.objects.all()
    for a in ServiceData:
        print(a.help_title)
    return render(request,'index.html')