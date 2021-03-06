# Generated by Django 3.2.13 on 2022-05-13 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('vol_num', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('street', models.CharField(blank=True, max_length=30)),
                ('apartment', models.CharField(blank=True, max_length=30)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('info', models.TextField(blank=True, max_length=500)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('manager', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.associationmanager')),
            ],
        ),
        migrations.CreateModel(
            name='volunteeringRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(max_length=500)),
                ('association', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='associations.association')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.helpouser')),
            ],
        ),
    ]
