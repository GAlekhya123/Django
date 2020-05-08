from django.shortcuts import render,redirect
from userapp.forms import Usersignupform
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
	if request.method=="POST":
		form = UsersignupForm(request.POST)

		#first_name=request.POST['first_name']
		#last_name=request.POST['last_name']
		#username=request.POST['username']
		#email=request.POST['email']
		#password1=request.POST['password1']
		#password2=request.POST['password2']
		#form=Usersignupform(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Done')
	form  = UsersignupForm()
	return render(request,'userapp/signup.html',{'form':form})


		#if password1==password2:
			#if User.objects.filter(username=username).exists():
				#print("username taken")
			#else:
				#user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
				#user.save()
				#print("user created")
		#else:
			#print("password not matching")
		#return render(request,'userapp/signup.html',{})
			
		
			
			
			
	form = Usersignupform()

	return render(request,'userapp/signup.html',{'form':form})
def home(request):
	return render(request,'userapp/home.html',{})
def profile(request):
	form=user.objects.get()
	return render(request,'userapp/profile.html',{'form':form})