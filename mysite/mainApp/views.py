from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ["Hello, please call me back later", "(099)0990809"]})
