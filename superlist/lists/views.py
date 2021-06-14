from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse


def home_page(request):
    """Домашняяя страница"""
    return render(request, 'lists/home.html')


def new_list(request):
    """Новый список"""
    Item.objects.create(text=request.POST['item_text'])
    return redirect('view_list')


def view_list(request):
    """Представление списка"""
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})

