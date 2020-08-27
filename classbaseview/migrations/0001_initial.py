# Generated by Django 3.0.8 on 2020-08-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=125)),
                ('Url', models.CharField(max_length=120)),
                ('Quote', models.CharField(max_length=220)),
                ('Star', models.CharField(max_length=20)),
            ],
        ),
    ]
