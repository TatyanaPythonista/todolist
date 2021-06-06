from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    """Домашняяя страница"""
    return HttpResponse('<html><title>To-Do list</title></html>')
