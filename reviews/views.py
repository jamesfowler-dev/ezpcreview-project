from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_review(request):
    return HttpResponse("I'm reviewing you!")