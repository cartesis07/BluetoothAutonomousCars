# Generated by Django 3.0.7 on 2020-06-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denm_cam', '0005_auto_20200623_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cam',
            name='test_binary',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='denm',
            name='test_binary',
            field=models.CharField(max_length=100),
        ),
    ]