# Generated by Django 2.0.2 on 2018-04-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20180410_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='login_name',
            field=models.CharField(max_length=15),
        ),
    ]
