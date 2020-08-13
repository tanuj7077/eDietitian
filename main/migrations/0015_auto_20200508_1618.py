# Generated by Django 3.0.3 on 2020-05-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200422_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='dtStatus',
            field=models.CharField(default='Diet not set yet.', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extenduser',
            name='macroStatus',
            field=models.CharField(default='Your Macronutrients not set currently. Calculate your macronutrients from the calculator given here.', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='bestFor',
            field=models.CharField(default='p', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='desc',
            field=models.CharField(default='a', max_length=500),
            preserve_default=False,
        ),
    ]
