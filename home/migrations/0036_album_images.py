# Generated by Django 4.1.1 on 2022-11-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_remove_album_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='Images',
            field=models.IntegerField(default=0),
        ),
    ]
