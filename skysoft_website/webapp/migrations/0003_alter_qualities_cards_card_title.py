# Generated by Django 5.1 on 2024-09-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_home_header_header_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualities_cards',
            name='card_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
