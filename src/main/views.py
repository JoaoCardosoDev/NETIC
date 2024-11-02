from django.shortcuts import render
from .context import context

def netics_home (request) :

    return render (request, "mainPage/index.html", context)

def profile(request):

    return render (request, "profilePage/index.html", context)