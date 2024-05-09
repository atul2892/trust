# Generated by Django 5.0.1 on 2024-05-09 10:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessQueryDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('businessName', models.CharField(blank='true', default='', max_length=500, null='true')),
                ('email', models.EmailField(blank='true', default='', max_length=254, null='true')),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=1000)),
                ('location', models.CharField(blank='true', default='', max_length=500, null='true')),
                ('query', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('email', models.EmailField(blank='true', default='', max_length=254, null='true')),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=1000)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DailyUpdate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('content', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank='true', default='', null='true', upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='MediaCoverage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('content', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('content', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank='true', default='', max_length=254, null='true')),
            ],
        ),
        migrations.CreateModel(
            name='OnLoadPopup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='SliderBanner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Speeche',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('content', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='VideosGallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('link', models.TextField(blank='true', default='', null='true')),
            ],
        ),
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('link', models.TextField()),
            ],
        ),
    ]
