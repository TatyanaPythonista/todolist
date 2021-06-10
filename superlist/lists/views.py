from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse


def home_page(request):
    """Домашняяя страница"""
    if request.method == "POST":
        new_item_text = request.POST["item_text"]
        Item.objects.create(text=new_item_text)
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'lists/home.html', {'items': items})

