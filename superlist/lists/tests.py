from django.test import TestCase
from .models import Item
from django.urls import resolve
from django.http import HttpRequest
from .views import home_page


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_uses_home_template(self):
        """Тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        """Тест: можно сохранить POST-запрос"""
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_POST(self):
        """Тест: переадресует после POST-запроса"""
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/only_one_list_in_the_world/')

    def test_only_saves_items_when_necessary(self):
        """Тест: сохраняет элементы, только когда нужно"""
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    """Тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """Тест сохранения и получения элементов списка"""
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0].text
        second_saved_item = saved_items[1].text
        self.assertEqual(first_saved_item, "The first (ever) list item")
        self.assertEqual(second_saved_item, "Item the second")


class ListViewTest(TestCase):
    """Тест представления списка"""

    def test_uses_list_templates(self):
        """Тест: используется шаблон списка"""
        response = self.client.get('/lists/only_one_list_in_the_world/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_all_list_items(self):
        """Тест: отображаются все элементы списка"""
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/lists/only_one_list_in_the_world/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')
