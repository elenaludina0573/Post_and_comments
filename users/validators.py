import re

from rest_framework.serializers import ValidationError


class PasswordValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, password):
        if not any(char.isdigit() for char in password):
            raise ValidationError(f'Пароль должен содержать хотя бы одну цифру')
        if len(password) < 8:
            raise ValidationError(f'Длина пароля должна составлять не менее 8 символов')


class EmailValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        if val and "mail.ru" or "yandex.ru" not in val:
            raise ValidationError(f'{self.field} должен использовать только домены "mail.ru" or "yandex.ru"')
