from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
def index(request):
    return render(request,"index.html")
def run(request):
    data=request.GET.get("data","default")
    name=request.GET.get("name","default")
    if len(name)==int(data):
        messages.success(request,"Welcome,Thankyou for visiting us, hope you like it!")
        return redirect("/bblock") 
    else:
        return HttpResponse("<h1>error!!</h1>")

