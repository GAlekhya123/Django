# Generated by Django 3.0.5 on 2020-05-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_auto_20200502_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='word',
            field=models.CharField(default='word@123', max_length=150),
        ),
    ]
