# Generated by Django 3.0.2 on 2020-01-27 17:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de création')),
            ],
            options={
                'verbose_name': 'Profil',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de création')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Profile')),
            ],
            options={
                'verbose_name': 'Statut',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.User'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de création')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Profile')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Status')),
            ],
            options={
                'verbose_name': 'Commentaire',
            },
        ),
    ]
