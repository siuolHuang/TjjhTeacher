from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
	return HttpResponse("Hello World!")

def hello_world_color(request):
	return render(request, 'hello_world.html',{
		'current_time': str(datetime.now()),
	})

# Create your views here.
