from django.forms import ModelForm
from .models import Userreg

class Student(ModelForm):
    class Meta:
        model = Userreg
        fields = ['firstname','lastname','username','mailid','phonenumber','age']