# Generated by Django 4.1.2 on 2022-11-01 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_post_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imgs',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
