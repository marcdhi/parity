from django.shortcuts import render
from django.http import HttpResponse


# Adding all views here:

def  main(request):
    return HttpResponse("Welcome to Music Controller API")
