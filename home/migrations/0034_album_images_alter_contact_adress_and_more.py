# Generated by Django 4.1.1 on 2022-11-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_contact_adress_alter_contact_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='Images',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Adress',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Company_Name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Facebook',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Instagram',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Latitude',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Linkedin',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Longitude',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='SMDescription',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='SMKeywords',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='SMTitle',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Telephone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Twitter',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Url',
            field=models.CharField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Website',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Whatsapp',
            field=models.CharField(max_length=15, null=True),
        ),
    ]