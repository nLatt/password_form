from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UserForm
# Create your views here.

def form(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("logged_in/")

    return render(request, "form.html", {"form": form})

def logged_in(request):
    return render(request, "logged_in.html")
