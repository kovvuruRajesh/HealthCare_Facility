# Generated by Django 3.0.5 on 2020-10-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCare_app', '0017_auto_20200622_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patientId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='assignedDoctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='patientId',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
