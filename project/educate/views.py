from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("This is hardcoded index page")

def courses(request):
    return HttpResponse("This is hardcoded courses page")

def lists(request):
    return HttpResponse("This is hardcoded lists page")

def article(request):
    return HttpResponse("This is hardcoded article page")
