from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mit(request):
    return render(request,'mit.html')

def contact(request):
    return render(request,'contactus.html')

def gallery(request):
    return render(request,'gallery.html')

def services(request):
    return render(request,'services.html')