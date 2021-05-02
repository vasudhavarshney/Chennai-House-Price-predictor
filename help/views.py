from django.shortcuts import render

# Create your views here.
def index(request):
	contaxt={'link':'http://127.0.0.1:8000/','a':'http://127.0.0.1:8000/register/','b':'http://127.0.0.1:8000/help/'}
	return render(request,'help.html',contaxt)