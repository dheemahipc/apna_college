# Generated by Django 5.0.4 on 2024-07-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_userdetails_delete_additionaldetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hw_version', models.CharField(max_length=255)),
                ('serial_no', models.CharField(max_length=255)),
                ('sw_version', models.CharField(max_length=255)),
                ('algo_version', models.CharField(max_length=255)),
                ('bootloader_version', models.CharField(max_length=255)),
                ('rest_bus', models.CharField(max_length=255)),
                ('release_update_mlc', models.CharField(max_length=255)),
                ('doors_test_spec_url', models.CharField(max_length=255)),
                ('doors_viewset', models.CharField(max_length=255)),
                ('ims_file_name_version', models.CharField(max_length=255)),
                ('test_engineer', models.CharField(max_length=255)),
                ('test_date', models.DateField()),
                ('reviewed_by', models.CharField(max_length=255)),
                ('review_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]
