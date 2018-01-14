from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class employees(models.Model):
   # name = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.firstname

class uploadem(models.Model):
    employee=models.ForeignKey(employees,on_delete=models.CASCADE,default=0)
    email=models.CharField(max_length=20)

    def __str__(self):
        return self.email


class uploadphone(models.Model):
    employee = models.ForeignKey(employees, on_delete=models.CASCADE, default=0)
    phone = models.IntegerField()

    def __str__(self):
        return str(self.phone)

class receiverequest(models.Model):
    request_id=models.ForeignKey(employees,on_delete=models.CASCADE,related_name='request_id') #Who sent friend request
    receive_id=models.ForeignKey(employees,on_delete=models.CASCADE,related_name='receive_id')#Who received friend request

    def __str__(self):
        return str(self.receive_id)

class Posts(models.Model):
     name=models.ForeignKey(employees,on_delete=models.CASCADE)
     #name=models.CharField(max_length=150,default='name')
     title=models.TextField(max_length=150)
     post=models.TextField()
     date=models.DateTimeField(default='')

     def __str__(self):
         return self.title

class Likes(models.Model):
    postliked=models.ForeignKey(Posts,on_delete=models.CASCADE)
    postlikedby=models.ForeignKey(employees,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Shares(models.Model):
    postshared = models.ForeignKey(Posts, on_delete=models.CASCADE)
    postsharedby = models.ForeignKey(employees, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)









