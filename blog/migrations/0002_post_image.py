# Generated by Django 4.1.7 on 2023-06-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='images/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]