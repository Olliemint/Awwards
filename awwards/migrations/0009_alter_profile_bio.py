# Generated by Django 4.0.5 on 2022-06-13 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0008_remove_projectdata_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
