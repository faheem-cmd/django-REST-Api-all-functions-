# Generated by Django 2.2.14 on 2021-09-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='news image/')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=10)),
                ('emp_id', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='employee/')),
            ],
        ),
    ]
