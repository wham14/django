from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mit(request):
    return render(request,'mit.html')

def contact(request):
    return render(request,'contactus.html')
