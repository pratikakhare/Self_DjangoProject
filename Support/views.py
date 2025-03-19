from django.shortcuts import render
from Support.models import SupportDesk
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def supportD(request):
    SupportDeskData = SupportDesk.objects.all()
    data = {
        'SupportDeskData':SupportDeskData
    }
    return render(request,'support.html',data)
