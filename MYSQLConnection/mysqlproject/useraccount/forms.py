from django.forms import ModelForm
from useraccount.models import Userregister

class Userregisterform(ModelForm):
	class Meta:
		model=Userregister
		fields=['fullname','image','mailid']
