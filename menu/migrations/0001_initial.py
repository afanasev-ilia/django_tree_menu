# Generated by Django 2.2.19 on 2023-10-06 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='укажите название меню', max_length=200, verbose_name='название меню')),
                ('slug', models.SlugField(help_text='укажите текстовый идентификатор меню', unique=True, verbose_name='текстовый идентификатор меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='ItemMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='укажите название пункта меню', max_length=200, verbose_name='название пункта меню')),
                ('slug', models.SlugField(help_text='укажите текстовый идентификатор пункта меню', unique=True, verbose_name='текстовый идентификатор пункта меню')),
                ('menu', models.ForeignKey(help_text='выберите меню', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu.Menu')),
                ('parent', models.ForeignKey(blank=True, help_text='выберите родительский пункт меню', on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='menu.ItemMenu')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]
