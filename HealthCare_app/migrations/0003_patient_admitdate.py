# Generated by Django 3.0.5 on 2020-05-18 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCare_app', '0002_delete_teacherextra'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='admitDate',
            field=models.DateField(auto_now=True),
        ),
    ]
