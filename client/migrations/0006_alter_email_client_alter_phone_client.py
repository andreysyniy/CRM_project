# Generated by Django 4.0 on 2022-01-11 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_alter_email_client_alter_phone_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_client', to='client.client'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phone_client', to='client.client'),
        ),
    ]