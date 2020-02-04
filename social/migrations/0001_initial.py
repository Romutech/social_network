# Generated by Django 3.0.2 on 2020-02-04 07:42

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, verbose_name='')),
                ('author', models.CharField(max_length=100, verbose_name='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de création')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, verbose_name='')),
                ('username', models.CharField(max_length=100, verbose_name='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de création')),
            ],
            options={
                'verbose_name': 'Profil',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileStatus',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='social.Message')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Profile')),
            ],
            options={
                'verbose_name': 'Statut',
            },
            bases=('social.message',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='social.Message')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.ProfileStatus')),
            ],
            options={
                'verbose_name': 'Commentaire',
            },
            bases=('social.message',),
        ),
    ]
