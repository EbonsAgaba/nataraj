from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(request, "<h1>Helo view</h1>", {})



