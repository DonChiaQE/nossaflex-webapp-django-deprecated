from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'nossaflexdb/login.html')

def signup(request):
    return render(request, 'nossaflexdb/signup.html')

def database(request):
    return render(request, 'nossaflexdb/database.html')