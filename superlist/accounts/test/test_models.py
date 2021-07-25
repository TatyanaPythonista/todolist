from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    """Тест модели пользователя"""

    def test_user_is_valid_with_email_only(self):
        """Тест: пользователь допустим только с электронной почты"""
        user = User(email='a@b.com')
        user.full_clean()  # не должно поднять исключение
