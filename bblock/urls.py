from django.contrib import admin
from django.urls import path,include
from . import views    


urlpatterns = [
    path("",views.first,name="first"), 
    path("About/",views.about,name="about"),
    path("learn/",views.learn,name="learn"),
    path("Founder/",views.founder,name="founder"),
    path("contact/",views.contact,name="contact"),
    path("members/",views.members,name="members"), 
    path("photo/",views.photo,name="photo"),
    path("signup/",views.handlesignup,name="handlesignup"),
    path("success/",views.success,name="success"),
    path("contactsuccess/",views.contactsuccess,name="contactsuccess"), 
    path("login/",views.handlelogin,name="handlelogin"), 
    path("logout/",views.handlelogout,name="handlelogout"), 
    path("exit/",views.exit,name="exit"),  
    path("induction/",views.induction,name="induction"),
    path("message/",views.message,name="message"),        
   

]  