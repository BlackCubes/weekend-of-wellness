# Generated by Django 5.0.2 on 2024-03-02 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0004_sponsors_sponsor_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsors',
            options={'verbose_name': 'Sponsor', 'verbose_name_plural': 'Sponsors'},
        ),
    ]
