# Generated by Django 4.1.7 on 2023-04-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_delhi_lat_remove_delhi_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='delhi',
            name='desc_field',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
