from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
	class Meta:
		model = Candidate
		fields = ["first_name", "last_name","email","massage"]
		fields= '__all__'

