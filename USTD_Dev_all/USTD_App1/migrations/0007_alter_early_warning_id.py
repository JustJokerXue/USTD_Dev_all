# Generated by Django 4.1.4 on 2022-12-24 02:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('USTD_App1', '0006_early_warning_alter_administrator_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='early_warning',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='学号'),
        ),
    ]
