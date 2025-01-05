from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def helloWord(request):
    return render(request,'signup.html',{'form':UserCreationForm()})