# Generated by Django 2.1.1 on 2018-10-05 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rallybooking', '0005_rally_updated_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rally',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='rally',
            name='published_by_name',
        ),
    ]