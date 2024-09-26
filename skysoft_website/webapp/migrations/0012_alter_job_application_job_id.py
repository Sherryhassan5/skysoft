# Generated by Django 5.1 on 2024-09-15 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_resume_job_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_application',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.job'),
        ),
    ]
