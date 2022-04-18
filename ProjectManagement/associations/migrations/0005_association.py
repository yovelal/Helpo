# Generated by Django 3.2.12 on 2022-04-18 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_rename_privacy_user_high_privacy'),
        ('associations', '0004_delete_association'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('vol_num', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('apartment', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('info', models.TextField(max_length=500)),
                ('manager', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.associationmanager')),
            ],
        ),
    ]
