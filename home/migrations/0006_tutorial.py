# Generated by Django 3.1.7 on 2021-04-15 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210414_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prerequisite', models.TextField()),
                ('steps', models.TextField()),
                ('date', models.DateTimeField()),
                ('script_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.script')),
            ],
        ),
    ]
