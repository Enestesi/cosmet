# Generated by Django 4.2.13 on 2024-05-26 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryservices',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услугу', 'verbose_name_plural': 'Услуги'},
        ),
    ]
