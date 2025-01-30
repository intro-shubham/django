# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("hello world! I'm Home Page")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("hello i am about page!")
    return render(request, 'about.html')
