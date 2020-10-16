from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact,Induction,Message 
from django.contrib.auth.models import User
from django.contrib import messages
from bblock.models import student
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def first(request):
    return render(request,"bblockmain.html")
def about(request):
    return render(request,"about.html")
def learn(request):
    return render(request,"learn.html")
def founder(request):
    return render(request,"founder.html")
def success(request):
    return render(request,"success.html")
def contactsuccess(request):
    return render(request,"contactsuccess.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name","default")
        college=request.POST.get("college","default")
        number=request.POST.get("number","default")
        town=request.POST.get("town","default")
        mail=request.POST.get("mail","default")
        text=request.POST.get("text","default")
        contact= Contact(name=name,college=college,number=number,town=town,mail=mail,text=text)
        contact.save()
        messages.success(request,"Your query has been sent to admin , we will look after it!")
        return redirect("/bblock")
    return render(request,"contact.html")
def photo(request):
    return render(request,"photo.html")
def handlesignup(request):
    if request.method=="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirmpassword=request.POST["confirmpassword"]
        myuser=User.objects.create_user(firstname,email,password)
        myuser.l_name=lastname
        myuser.conf_password=confirmpassword
        myuser.save()
        messages.success(request,"Thankyou for signing up!, your request has been sent to the user!")
        return redirect("/bblock/")


    else:
        return HttpResponse("not found")
def handlelogin(request):
     name=request.POST["yourname"]
     password=request.POST["yourpassword"]
     user=authenticate(username=name,password=password)
     if user is not None:
         login(request,user)
         messages.success(request,"suceesfully loged in!")
         return render(request,"induction.html")
     else:
        messages.error(request,"paasword is incorrect!")
        return redirect("/bblock")

def handlelogout(request):
    logout(request)
    messages.success(request,"Successfully logged out ,Thankyou for showing interest ")
    return redirect("/bblock")
    
def members(request):
    return render(request,"members.html")
def exit(request):
    sure=request.GET.get("sure","off")
    if sure=="on":
        return redirect("/")
    else:
        return render(request,"/bblock")
def induction(request):
    if request.method=="POST":
        name=request.POST.get("name","default")
        branch=request.POST.get("branch","default")
        description=request.POST.get("description","default")
        cgpa=request.POST.get("cgpa","default")
        mail=request.POST.get("mail","default")
        text=request.POST.get("text","default")
        instagram=request.POST.get("instagram","default")
        induction= Induction(name=name,branch=branch,cgpa=cgpa,mail=mail,description=description,text=text,instagram=instagram)
        induction.save()
        messages.success(request,"Your induction letter have been sent, we will let you know the results through your email")
        return redirect("/bblock")
    else:
        return HttpResponse("ERROR!!")
def message(request):
    if request.method=="POST":
        name=request.POST["name"]
        password=request.POST["password"]
        message=request.POST["message"]
        user=authenticate(username=name,password=password)
        if user is not None:
            message=Message(name=name,password=password,message=message)
            message.save()
            messages.success(request,"Your message is sent to the admin, Thanks for your interest.")
            return redirect("/bblock")
        else:
            messages.success(request,"Sorry user not found!")
            return redirect("/bblock")




