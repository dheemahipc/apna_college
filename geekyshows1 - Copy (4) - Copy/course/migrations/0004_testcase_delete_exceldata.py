# Generated by Django 5.0.4 on 2024-05-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_exceldata_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=255)),
                ('test_name', models.CharField(max_length=255)),
                ('test_result', models.CharField(max_length=255)),
                ('screenshot_description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ExcelData',
        ),
    ]
