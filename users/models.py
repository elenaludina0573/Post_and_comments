from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    login = models.CharField(max_length=150, verbose_name='Логин', unique=True)
    password = models.CharField(max_length=100, verbose_name='Пароль')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    date_birth = models.DateField(max_length=15, verbose_name='Дата рождения', **NULLABLE)
    email = models.EmailField(verbose_name='Почта', unique=True)
    date_creation = models.DateField(max_length=15, verbose_name='Дата создания', auto_now_add=True)
    date_editing = models.DateField(max_length=15, verbose_name='Дата редактирования', auto_now_add=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.login}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
