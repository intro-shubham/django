# Generated by Django 5.1.5 on 2025-01-31 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_options_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
    ]
