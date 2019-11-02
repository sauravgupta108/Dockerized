from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def index(request):
	return HttpResponse("<b><i>This is Delhi. Now changing.</i></b>")
