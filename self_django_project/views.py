from django.http import HttpResponse
from django.shortcuts import render
def first(request):
    return HttpResponse("<b>Hello, world. You're at the first index.</b>")

def home(request):
    
    data = {
        'title':'Home Page',
        'text':'Welcome to the home page',
        'number':100,
        'clist':['python','django','JAva','C++','C#'],
        'stu_det':[
            {'name':'John','age':25},
            {'name': 'Doe', 'age': 30},
        ]
    }
    return render(request,"index.html", data)

def userform(request):
    total = 0
    try:
        n1 = int(request.GET.get('num1'))
        n2 = int(request.GET.get('num2'))
        total = n1 + n2
    except:
        pass    
    return render(request,"userform.html", {'total':total})