# Generated by Django 4.1.2 on 2022-11-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='learner',
            fields=[
                ('AssessmentNumber', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Assessment Number')),
                ('FullName', models.CharField(max_length=100, verbose_name='Full Name')),
                ('BirthCertificateNumber', models.CharField(max_length=30, verbose_name='Birth Certificate Number')),
                ('Gender', models.CharField(max_length=1, verbose_name='Gender')),
                ('YearOfBirth', models.IntegerField(verbose_name='YearOfBirth')),
            ],
            options={
                'ordering': ['AssessmentNumber', 'FullName'],
            },
        ),
    ]
