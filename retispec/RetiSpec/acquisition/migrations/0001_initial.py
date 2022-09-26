# Generated by Django 4.1.1 on 2022-09-26 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0002_alter_patient_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acquisition',
            fields=[
                ('AcquisitionID', models.AutoField(primary_key=True, serialize=False)),
                ('SiteName', models.CharField(blank=True, max_length=50, null=True)),
                ('DateTaken', models.DateField()),
                ('OperatorName', models.CharField(blank=True, max_length=50, null=True)),
                ('ImageData', models.ImageField(blank=True, null=True, upload_to='ImageData')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
