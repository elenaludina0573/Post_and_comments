import re

from rest_framework.serializers import ValidationError


class PasswordValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, password):
        reg = re.compile(r"[0-9]")
        tmp_val = dict(password).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError(f'Пароль должен содержать хотя бы одну цифру')
        if len(password.get(self.field)) < 8:
            raise ValidationError(f'Длина пароля должна составлять не менее 8 символов')


class EmailValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        allowed_domains = ["mail.ru", "yandex.ru"]
        if any(word in value for word in allowed_domains):
            raise ValidationError(f"Разрешены следующие домены {', '.join(allowed_domains)}")
