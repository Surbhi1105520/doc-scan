from django.shortcuts import render, HttpResponse
#create your views here
def index(request):  
    return render(request, 'index.html')

