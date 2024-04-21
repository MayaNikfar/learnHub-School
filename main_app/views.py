from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def careers(request):
    return render(request, 'careers.html')

def blog(request):
    return render(request, 'blog.html')

def login(request):
    return render(request, 'login.html')


