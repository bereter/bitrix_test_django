# Generated by Django 5.0.4 on 2024-04-21 20:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('category', models.CharField(choices=[('va', 'Вакансия'), ('or', 'Заказ')], max_length=2, unique=True, verbose_name='Категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL, verbose_name='Пост')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.post', verbose_name='Пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
