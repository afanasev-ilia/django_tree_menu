# Generated by Django 2.2.19 on 2023-10-06 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmenu',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='выберите родительский пункт меню', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='menu.ItemMenu'),
        ),
    ]
