# Generated by Django 5.0.4 on 2024-04-29 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replypost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='work.post', verbose_name='Пост'),
        ),
    ]