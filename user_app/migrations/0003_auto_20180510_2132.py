# Generated by Django 2.0.2 on 2018-05-10 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_app.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='org',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_app.Organization'),
            preserve_default=False,
        ),
    ]