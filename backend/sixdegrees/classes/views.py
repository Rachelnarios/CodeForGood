from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "classes/UI/Webpage/examples/landing-page.html")
