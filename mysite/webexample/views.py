from django.shortcuts import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h3>Hello</h3>")