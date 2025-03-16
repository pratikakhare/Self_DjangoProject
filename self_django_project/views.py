from django.http import HttpResponse

def first(request):
    return HttpResponse("<b>Hello, world. You're at the first index.</b>")