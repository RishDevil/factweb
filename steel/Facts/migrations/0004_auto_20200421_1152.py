# Generated by Django 3.0.1 on 2020-04-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facts', '0003_link_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=models.SlugField(),
        ),
    ]
