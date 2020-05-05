from django.db import models

# Create your models here.
class Userreg(models.Model):
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	username=models.CharField(max_length=100,unique=True)
	password=models.CharField(max_length=100)
	mailid=models.EmailField()
	phonenumber=models.CharField(max_length=12,unique=True)
	age=models.IntegerField()
def __str__(self):
	return self.username
