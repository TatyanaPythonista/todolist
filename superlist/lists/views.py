from django.shortcuts import render, redirect
from .models import Item, List
from django.http import HttpResponse


def home_page(request):
    """Домашняяя страница"""
    return render(request, 'lists/home.html')


def new_list(request):
    """Новый список"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('view_list')


def view_list(request):
    """Представление списка"""
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})

