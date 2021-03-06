from django.shortcuts import render, redirect
from lists.forms import ItemForm, EMPTY_ITEM_ERROR, ExistingListItemForm
from .models import Item, List
from django.core.exceptions import ValidationError


def home_page(request):
    """Домашняяя страница"""
    return render(request, 'lists/home.html', {'form': ItemForm()})


def new_list(request):
    """Новый список"""
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'lists/home.html', {'form': form})


def view_list(request, list_id):
    """Представление списка"""
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save(for_list=list_)
            return redirect(list_)
    return render(request, 'lists/list.html', {'list': list_, 'form': form})
