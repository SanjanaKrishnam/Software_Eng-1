# Generated by Django 2.0.2 on 2018-03-07 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('profiledet', '0013_auto_20180307_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]