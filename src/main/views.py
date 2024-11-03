from django.shortcuts import redirect, render

from .forms import ProfileForm
from .context import context

def netics_home (request) :

    return render (request, "mainPage/index.html", context)

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        context["form"] = ProfileForm()

    return render (request, "profilePage/index.html", context)