# Generated by Django 3.1.3 on 2020-11-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('team', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('bio', models.TextField(max_length=500)),
            ],
        ),
    ]