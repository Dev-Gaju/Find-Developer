from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects(request):
    return HttpResponse("Here Our Products")


def project(request, pk):
    return HttpResponse("Single Project" + '  ' + str(pk))
