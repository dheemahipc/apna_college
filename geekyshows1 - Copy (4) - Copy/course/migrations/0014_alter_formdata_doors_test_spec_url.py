# Generated by Django 5.0.4 on 2024-07-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_formdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='doors_test_spec_url',
            field=models.URLField(max_length=255),
        ),
    ]
