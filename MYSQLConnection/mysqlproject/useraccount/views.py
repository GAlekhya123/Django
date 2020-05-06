from django.shortcuts import render
from useraccount.forms import Userregisterform
from django.http import HttpResponse
from useraccount.models import Userregister
from django.core.mail import send_mail
from mysqlproject import settings


# Create your views here.
def upload(request):
	if request.method=='POST':
		form=Userregisterform(request.POST,request.FILES)
		print(form.is_valid())
		if form.is_valid():
			#form.save()
			fullname=request.POST.get('fullname')
			mailid=request.POST.get('mailid')
			word=fullname+'@123'
			model=Userregister(fullname=fullname,mailid=mailid,image=request.FILES['image'],word=word)
			model.save()
			sub="hi"
			body='this is your mailid '+mailid+' and this is your password '+word
			receiver=request.POST['mailid']
			sender=settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[receiver])
			return HttpResponse("password")
			return HttpResponse("Image Uploaded")
	form=Userregisterform()
	return render(request,'useraccount/upload.html',{'form':form}) 
def display(request):
	data=Userregister.objects.all()
	return render(request,'useraccount/displayimages.html',{'data':data})
def showall(request):
	data = Userregister.objects.all()
	return render(request,'useraccount/showall.html',{'data':data})
		
def details(request,id):
	data = Userregister.objects.get(id = id)
	return render(request,'userAccount/details.html',{'data':data})