# Generated by Django 2.0.2 on 2018-05-10 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_auto_20180510_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagged_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.Article')),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
        migrations.AddField(
            model_name='tagged_article',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.Tag'),
        ),
    ]