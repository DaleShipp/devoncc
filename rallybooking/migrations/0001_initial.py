# Generated by Django 2.1.1 on 2018-10-05 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Rally',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rally_name', models.CharField(max_length=300)),
                ('rally_no', models.IntegerField()),
                ('added_date', models.DateTimeField(verbose_name='date added')),
                ('pub_date', models.DateTimeField(verbose_name='date published for booking')),
                ('added_by_name', models.CharField(max_length=300)),
                ('published_by_name', models.CharField(max_length=300)),
                ('num_pitches_total', models.IntegerField(default=1)),
                ('num_powered_pitches', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField(verbose_name='first night')),
                ('end_date', models.DateTimeField(verbose_name='last night')),
                ('leave_time', models.TimeField(default='16:00', verbose_name='time to leave site')),
                ('dogs_allowed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RallyBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rallybooking.Question'),
        ),
    ]
