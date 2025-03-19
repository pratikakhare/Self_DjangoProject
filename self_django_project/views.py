from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from service.models import help,Card
from .forms import userForm

def first(request):
    return HttpResponse("<b>Hello, world. You're at the first index.</b>")

# def home(request):
    
#     data = {
#         'title':'Home Page',
#         'text':'Welcome to the home page',
#         'number':100,
#         'clist':['python','django','JAva','C++','C#'],
#         'stu_det':[
#             {'name':'John','age':25},
#             {'name': 'Doe', 'age': 30},
#         ]
#     }
#     return render(request,"index.html", data)

# def userform(request):
#     finalans = 0
#     fn = userForm()
    # data = {'form':fn}
    # try:
    #     if request.method == 'POST':
    #         n1 = int(request.POST['num1'])
    #         n2 = int(request.POST['num2'])
    #         finalans = n1 + n2
    #         data = {
    #             'form': fn,
    #             'n1':n1,
    #             'n2':n2,
    #             'ans': finalans,
    #        }
    #         url = "/userform/?output={}".format(finalans)
    #         return HttpResponseRedirect(url)
            
    # except:
    #     pass
    #     return render(request,"userform.html",data)

def calculator(request):
    cal = ''
    try:
        if request.method == "POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            opr=request.POST.get('opr')
            
            if opr == '+':
                cal=n1+n2
            elif opr == '-':
                cal=n1-n2
            elif opr == '*':
                cal=n1*n2
            elif opr =='/':
                cal=n1/n2
    except:
        cal = "Invalid Input...!"
        print(cal)
    return render(request,"calculator.html",{'cal':cal})


