from django.db import models

# Create your models here.

class student(models.Model):
    student_id=models.AutoField
    student_name=models.CharField(max_length=50,default="")
    des=models.CharField(max_length=400,default="")
    branch=models.CharField(max_length=50,default="")
    speciality=models.CharField(max_length=50,default="")
    code=models.IntegerField(default=0)
    image=models.ImageField(upload_to="static",default="")
    instagram=models.CharField(max_length=50,default="")
    Facebook=models.CharField(max_length=50,default="")
 
    def __str__(self):
        return self.student_name

class founder(models.Model):
    founder_id=models.AutoField
    founder_name=models.CharField(max_length=50)
    des=models.CharField(max_length=300)
    branch=models.CharField(max_length=50,default="")
    image=models.ImageField(upload_to="static",default="")
    facebbok_name=models.CharField(max_length=30)
    home_town=models.CharField(max_length=30)

    def __str__(self):
        return self.founder_name

class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    college=models.CharField(max_length=400)
    town=models.CharField(max_length=50,default="")
    mail=models.CharField(max_length=50,default="")
    number=models.IntegerField(default=0)
    text=models.CharField(max_length=500,default="")
   

    def __str__(self):
        return self.name


class Induction(models.Model):
    induction_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=400)
    description=models.CharField(max_length=50,default="")
    mail=models.CharField(max_length=50,default="")
    cgpa=models.IntegerField(default=0)
    instagram=models.CharField(max_length=50,default="")
    text=models.CharField(max_length=500,default="")
   

    def __str__(self):
        return self.name
class Message(models.Model):
    message_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=400)
    message=models.CharField(max_length=700,default="")
   
   

    def __str__(self):
        return self.name