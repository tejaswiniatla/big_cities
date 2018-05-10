# Generated by Django 2.0.2 on 2018-05-10 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20180510_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagged_article',
            name='article',
        ),
        migrations.RemoveField(
            model_name='tagged_article',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(to='user_app.Article'),
        ),
        migrations.DeleteModel(
            name='Tagged_article',
        ),
    ]
