# Generated by Django 5.0.6 on 2024-05-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('ingredient', models.CharField(max_length=400)),
                ('prix', models.FloatField(default=0.0)),
                ('vegetarienne', models.BooleanField(default=False)),
            ],
        ),
    ]
