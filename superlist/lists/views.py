from django.shortcuts import render, redirect
from .models import Item, List
from django.core.exceptions import ValidationError


def home_page(request):
    """Домашняяя страница"""
    return render(request, 'lists/home.html')


def new_list(request):
    """Новый список"""
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'lists/home.html', {'error': error})
    return redirect('view_list', list_.id)


def view_list(request, list_id):
    """Представление списка"""
    list_ = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'list': list_})


def add_item(request, list_id):
    """Добавить элемент"""
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
