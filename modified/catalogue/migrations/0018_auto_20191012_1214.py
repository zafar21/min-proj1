# Generated by Django 2.2.6 on 2019-10-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0017_auto_20190816_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='aspect_ratio',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='horizontal_pix',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='panel_type',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='refresh_rate',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='resolution',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='response_time',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='screen_size',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='vertical_pix',
            field=models.IntegerField(null=True),
        ),
    ]
