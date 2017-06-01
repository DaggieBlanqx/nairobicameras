from django.shortcuts import render

from forms import ContactForm
from django.contrib.auth.decorators import login_required


def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		print form.cleaned_data

	context = {
	"form": form,
	"title": title,

	}
	return render(request, "contact.html", context)
