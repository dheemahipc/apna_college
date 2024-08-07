# Generated by Django 5.0.4 on 2024-07-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0007_delete_exceldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
            ],
        ),
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
    ]
