from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, djrecipes!")


def about(request):
    return HttpResponse("About djrecipes")