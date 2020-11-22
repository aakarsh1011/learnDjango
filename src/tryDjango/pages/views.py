from django.shortcuts import render
from django.http import HttpResponse	# to give out html as httpresponse

# Create your views here.
# Create views by making function

def home_view(*args, **kwargs):
	return HttpResponse("<h1> Hello World </h1>")

def contact_view(*args, **kwargs):
	return HttpResponse("<h1> Contact </h1>")

def about_view(*args, **kwargs):
	return HttpResponse("<h1> About </h1>")
