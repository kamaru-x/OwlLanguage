# Generated by Django 4.1.1 on 2022-10-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_product_refer_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='Refer_number',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
