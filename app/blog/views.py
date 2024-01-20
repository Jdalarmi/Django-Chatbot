from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return render(request)
