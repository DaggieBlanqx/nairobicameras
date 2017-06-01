from django import forms
from django.forms import ModelForm, Textarea

from .models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['full_name', 'email', 'message']

		widgets = {
            'message': Textarea(attrs={'cols': 20, 'rows': 20}),
        }

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name
	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email		