# Generated by Django 3.1.2 on 2020-10-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201006_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='fotos/', verbose_name='foto'),
        ),
    ]
