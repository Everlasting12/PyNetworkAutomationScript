# Generated by Django 3.1.7 on 2021-04-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_tutorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
