# Generated by Django 5.0.4 on 2024-07-24 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_formdata_doors_document_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formdata',
            old_name='doors_document',
            new_name='input1',
        ),
        migrations.RenameField(
            model_name='formdata',
            old_name='test_description_url',
            new_name='input2',
        ),
    ]
