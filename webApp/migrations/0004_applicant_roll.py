# Generated by Django 5.1 on 2024-08-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_remove_applicant_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='roll',
            field=models.IntegerField(default=None),
        ),
    ]
