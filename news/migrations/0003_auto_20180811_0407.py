# Generated by Django 2.0.5 on 2018-08-11 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
