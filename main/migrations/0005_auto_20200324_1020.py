# Generated by Django 3.0.3 on 2020-03-24 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200324_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='unit',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
