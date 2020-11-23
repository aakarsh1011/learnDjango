from django.shortcuts import render
from django.http import HttpResponse	# to give out html as httpresponse

# Create your views here.
# Create views by making function

def home_view(request,*args, **kwargs):
	return render(request, "home.html",{})

def contact_view(request,*args, **kwargs):
	return render(request, "contact.html",{})

def about_view(request,*args, **kwargs):
	return render(request, "about.html", {})
