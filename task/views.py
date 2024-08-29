from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm


# Create your views here.

def helloword(request):
    return render(request, "signup.html",{
        'form': UserChangeForm
    })
