# Generated by Django 2.1.1 on 2018-10-05 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rallybooking', '0006_auto_20181005_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='rally',
            name='site_name',
            field=models.CharField(default='', max_length=300),
        ),
    ]