from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Post(models.Model):
    """Пост"""
    vacancy = 'va'
    order = 'or'

    CATEGORY_POST = [
        (vacancy, 'Вакансия'),
        (order, 'Заказ')
    ]

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    price = models.IntegerField(default=0, verbose_name='Цена')
    category = models.CharField(max_length=2, choices=CATEGORY_POST, unique=True, verbose_name='Категория')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', verbose_name='Пост')

    def __str__(self):
        return f'{self.user.username}: {self.name}'


class ReplyPost(models.Model):
    """Отклик"""
    description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')

    def __str__(self):
        return f'Отклик {self.user.username} на - {self.post.name}'


class BaseRegisterForm(UserCreationForm):
    """Форма регистрации пользователя"""

    email = forms.EmailField(lable='Email')

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
                  )