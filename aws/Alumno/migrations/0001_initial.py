# Generated by Django 2.2.7 on 2019-11-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('edad', models.CharField(max_length=254)),
                ('direccion', models.CharField(max_length=254)),
                ('sexo', models.CharField(max_length=254)),
                ('apellidoPaterno', models.CharField(max_length=254)),
                ('apellidoMaterno', models.CharField(max_length=254)),
                ('carrera', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'Alumno',
            },
        ),
    ]
