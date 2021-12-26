# Generated by Django 4.0 on 2021-12-26 21:01

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='client',
            name='company_name',
            field=models.CharField(max_length=100, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_change',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='client',
            name='full_name_director',
            field=models.CharField(max_length=100, verbose_name='Ф.И.О. директора'),
        ),
        migrations.AlterField(
            model_name='client',
            name='short_description',
            field=tinymce.models.HTMLField(max_length=300, verbose_name='Краткое описание'),
        ),
    ]
