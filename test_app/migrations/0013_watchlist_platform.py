# Generated by Django 3.2.7 on 2021-10-23 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0012_auto_20211022_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='test_app.streamplatform'),
            preserve_default=False,
        ),
    ]
