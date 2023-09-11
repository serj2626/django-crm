from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='profile')

    def __str__(self):
        return f'Профиль {self.user}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'
