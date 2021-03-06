# Generated by Django 3.0.3 on 2020-03-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calorie',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='carbohydrate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='fat',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='protein',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
