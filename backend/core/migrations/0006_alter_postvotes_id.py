# Generated by Django 3.2.11 on 2022-01-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220114_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postvotes',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]