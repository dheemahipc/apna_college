# Generated by Django 5.0.4 on 2024-05-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_testcase_delete_exceldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
            ],
        ),
    ]
