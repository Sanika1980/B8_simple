from django.shortcuts import render

# Create your views here.

def home(request):
    data = {"greeting":"Hello world"}
    return render(request,"base.html", context=data)