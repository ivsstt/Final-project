# Generated by Django 4.2.1 on 2023-05-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(verbose_name='Зарплата'),
        ),
    ]
