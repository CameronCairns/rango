from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#The context_dict is passed as an argument to the render function so that any django 
	#template variable can be appropriately supplied
	context_dict = { 'boldmessage' : "I am bold font from the context"}

	#Render will give the user the modified template based on the context for the
	#template variable which is supplied as a paramater
	return render(request,'mrango/index.html', context_dict)
def about(request):
	#The context_dict is passed as an argument to the render function so that any django 
	#template variable can be appropriately supplied
	context_dict = { 'boldmessage' : "I am bold font from the about page"}

	#Render will give the user the modified template based on the context for the
	#template variable which is supplied as a paramater
	return render(request,'mrango/about.html', context_dict)