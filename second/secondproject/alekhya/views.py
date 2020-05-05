from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .forms import Student
from .models import Userreg
from django.contrib import messages

# Create your views here.
def hello(request):
    return HttpResponse('hello')

def register(request):
    if request.method == 'POST':
        form = Student(request.POST)
        if form.is_valid():
            # import pdb;pdb.set_trace()
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            password = lastname+"123"
            username = request.POST.get('username')
            mailid = request.POST.get('mailid')
            phonenumber = request.POST.get('phonenumber')
            age = request.POST.get('age')
            #import pdb;pdb.set_trace()
            model = Userreg(firstname=firstname,lastname=lastname,password=password,username=username,mailid=mailid,phonenumber=phonenumber,age=age)
            model.save()
            # messages.success(request,'User Details added Successfully')
            return HttpResponse("your password is : "+'"'+password+'"')
        else:
            messages.warning(request,'please enter valid details!!')
            return render(request,'alekhya/register.html',{'form':form})
    form = Student()
    return render(request,'alekhya/register.html',{'form':form})

def login(request):
    if request.method == "POST":
        data = Userreg.objects.get(username = request.POST['username'])
        messages.success(request,'Login successful!! :)')
        return render(request,'details.html',{'data':data})
    return render(request,'login.html',{})


        
	  







