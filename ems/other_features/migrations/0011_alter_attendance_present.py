# Generated by Django 4.0.6 on 2023-01-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other_features', '0010_alter_salary_working_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='present',
            field=models.BooleanField(default=False),
        ),
    ]
