# Generated by Django 2.2.6 on 2019-10-12 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0018_auto_20191012_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='aspect_ratio',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='horizontal_pix',
        ),
        migrations.RemoveField(
            model_name='product',
            name='panel_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='refresh_rate',
        ),
        migrations.RemoveField(
            model_name='product',
            name='resolution',
        ),
        migrations.RemoveField(
            model_name='product',
            name='response_time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='screen_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vertical_pix',
        ),
    ]
