# Generated by Django 4.1.4 on 2022-12-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
