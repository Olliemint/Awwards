# Generated by Django 4.0.5 on 2022-06-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdata',
            name='project_image',
            field=models.ImageField(default='project.jpg', upload_to='projectpics'),
        ),
        migrations.AlterField(
            model_name='projectdata',
            name='project_link',
            field=models.URLField(max_length=500),
        ),
    ]
