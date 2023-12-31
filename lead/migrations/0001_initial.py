# Generated by Django 4.2.5 on 2023-09-11 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=10, verbose_name='приоритет')),
                ('status', models.CharField(choices=[('new', 'New'), ('contacted', 'Contacted'), ('won', 'Won'), ('lost', 'Lost')], default='new', max_length=10, verbose_name='статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='изменено')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads', to=settings.AUTH_USER_MODEL, verbose_name='клиенты')),
            ],
            options={
                'verbose_name': 'Клиенты',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
