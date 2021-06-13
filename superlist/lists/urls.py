from django.urls import path
from .views import home_page, view_list

urlpatterns = [
    path('', home_page, name='name'),
    path('lists/only_one_list_in_the_world/', view_list, name='view_list'),
]
