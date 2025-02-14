# Generated by Django 2.2.4 on 2019-08-31 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NBAHotNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NewsId', models.IntegerField()),
                ('NewsTitle', models.CharField(max_length=60)),
                ('NewsDetailUrl', models.URLField()),
                ('NewsUpdateDateTime', models.DateTimeField()),
                ('ImgUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='NBAHotNewsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=30)),
                ('NewsContent', models.TextField()),
                ('ImageUrl', models.URLField()),
                ('MainNews', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NBAHotNewsApp.NBAHotNews')),
            ],
        ),
    ]
