# Generated by Django 2.2.1 on 2019-06-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190605_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='reader_num',
            field=models.IntegerField(default=0),
        ),
    ]
