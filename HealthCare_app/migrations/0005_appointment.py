# Generated by Django 3.0.5 on 2020-05-20 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCare_app', '0004_patientdischargedetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField()),
                ('doctorId', models.PositiveIntegerField()),
                ('appointmentDate', models.DateField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
