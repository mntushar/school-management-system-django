# Generated by Django 2.2.8 on 2020-07-29 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20200716_0518'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('bord', models.CharField(blank=True, max_length=15, null=True)),
                ('gpa', models.IntegerField()),
            ],
        ),
    ]
