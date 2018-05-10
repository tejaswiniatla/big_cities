# Generated by Django 2.0.2 on 2018-05-10 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20180510_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagged_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_app.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_keyword',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='tagged_article',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.Article'),
        ),
        migrations.AddField(
            model_name='tagged_article',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.Tag'),
        ),
    ]