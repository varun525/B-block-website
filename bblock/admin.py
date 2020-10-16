from django.contrib import admin

# Register your models here.
from .models import student
from .models import founder
from .models import Contact,Induction,Message
admin.site.register(student)  
admin.site.register(founder) 
admin.site.register(Contact)
admin.site.register(Induction)
admin.site.register(Message) 
