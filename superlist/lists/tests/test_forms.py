from django.test import TestCase
from lists.forms import ItemForm, EMPTY_ITEM_ERROR


class ItemFormTest(TestCase):
    """Тест формы для элемента списка"""

    def test_form_item_input_has_placeholder_and_css_classes(self):
        """Тест: поле ввода имеет атрибут placeholder и css-классы"""
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        """Тест валидации формы для пустых элементов"""
        form = ItemForm(data={'test': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [EMPTY_ITEM_ERROR]
        )
