# Generated by Django 2.0.9 on 2018-11-06 17:16

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                  parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(
                    max_length=100, verbose_name='Municipio')),
                ('estado', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='usuarios.Estado')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='estado',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='usuarios.Estado'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='municipio',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='usuarios.Municipio'),
        ),
    ]
