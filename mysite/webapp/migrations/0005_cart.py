# Generated by Django 2.2.14 on 2021-09-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
