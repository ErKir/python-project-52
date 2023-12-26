# Generated by Django 5.0 on 2023-12-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
