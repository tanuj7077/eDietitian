# Generated by Django 3.0.3 on 2020-05-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200509_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='bestFor',
            field=models.CharField(max_length=2),
        ),
    ]
