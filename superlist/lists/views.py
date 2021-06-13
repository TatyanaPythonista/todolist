from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse


def home_page(request):
    """Домашняяя страница"""
    if request.method == "POST":
        new_item_text = request.POST["item_text"]
        Item.objects.create(text=new_item_text)
        return redirect('/lists/only_one_list_in_the_world/')
    return render(request, 'lists/home.html')


def view_list(request):
    """Представление списка"""
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})

