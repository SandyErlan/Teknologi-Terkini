# Generated by Django 4.1.4 on 2022-12-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karya', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.TextField(blank=True, max_length=100, null=True)),
                ('tanggal', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('conten', models.TextField(blank=True, null=True)),
                ('img', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]