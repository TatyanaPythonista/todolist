from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self):
        """Установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: Можно начать список и получить его позже"""
        # Эдит слышала про крутое новое онлайн-приложение со списком неотложных дел.
        # Она решает оценить его домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о стисках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ей сразу же предлагается ввести элемент списка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Она набирает в текстовом поле "Купить павлинья перья" (её хобби - вязание рыболовных мушек)
        inputbox.send_keys('Купить павлиньи перья')

        # Когда она нажимает enter, страница обновляется, и теперь страница содержит:
        # "1: Купить павлинья перья" в качестве элемента списка.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_elements_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Купить павлинья перья' for row in rows)
        )

        # Текстовое поле по-прежнему приглашает её добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиных перьев"
        # (Эдит очень методична)
        self.fail('Закончить тест!')

# Страница снова обновляется, и теперь показывает оба элемента списка

# Эдит интересно, запомнит ли сайт ее списокю Далее она видит, что сайт сгенерировал для нее уникальный
# url-адрес - об этом выводится небольшой текст с объяснениями.

# Она посещает этот url-адрес - её список по-прежнему там.

# Удоблетворенная, она снова ложится спать.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
