from django.urls import path
from .views import home_page, view_list, new_list

urlpatterns = [
    path('', home_page, name='name'),
    path('lists/new/', new_list, name='new_list'),
    path('lists/only_one_list_in_the_world/', view_list, name='view_list'),
]
