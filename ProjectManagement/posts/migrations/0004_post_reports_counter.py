# Generated by Django 3.2.13 on 2022-05-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220506_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reports_counter',
            field=models.IntegerField(default=0),
        ),
    ]
