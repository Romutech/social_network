# Generated by Django 3.0.2 on 2020-02-03 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
    ]