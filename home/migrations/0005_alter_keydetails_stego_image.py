# Generated by Django 4.1.5 on 2023-02-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_keydetails_stego_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keydetails',
            name='stego_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
