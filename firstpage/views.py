from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	return render(request,'homepage.html',{'link':'http://127.0.0.1:8000/','a':'http://127.0.0.1:8000/register/','b':'http://127.0.0.1:8000/help/'})
	

