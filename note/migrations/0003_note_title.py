# Generated by Django 3.0.8 on 2020-07-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20200720_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='Unknow Title', max_length=50),
        ),
    ]
