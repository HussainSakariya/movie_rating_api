# Generated by Django 2.2.9 on 2020-09-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieratingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
