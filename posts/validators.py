from datetime import datetime
from rest_framework.serializers import ValidationError

forbidden_words = [
    'ерунда', 'глупость', 'чепуха'
]


class TitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if any(word in value for word in forbidden_words):
            raise ValidationError(f"Заголовок {value} содержит запрещенные слова.")


class AuthorValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        value = datetime.strptime(value, "%Y-%m-%d").date()
        today = datetime.today()
        age = (today.year - value.year - ((today.month, today.day) < (value.month, value.day)))
        if age < 18:
            raise ValidationError(f"Автор должен быть не моложе 18 лет.")
