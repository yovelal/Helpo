# Generated by Django 4.0.3 on 2022-04-29 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(max_length=500)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('is_asking', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.helpouser')),
            ],
        ),
    ]
