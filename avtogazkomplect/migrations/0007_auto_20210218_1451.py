# Generated by Django 3.1.6 on 2021-02-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avtogazkomplect', '0006_auto_20210218_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='', verbose_name='Ссылка картинки'),
        ),
    ]
