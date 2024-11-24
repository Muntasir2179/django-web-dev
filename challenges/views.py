from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for the entire month!")


def february(request):
    return HttpResponse("Walk for at least 20 minutes every day.")


def march(request):
    return HttpResponse("Learn Django for at least 20 min.")
