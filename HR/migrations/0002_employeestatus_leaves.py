# Generated by Django 4.1.5 on 2023-04-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeestatus',
            name='leaves',
            field=models.IntegerField(default=14, null=True),
        ),
    ]
