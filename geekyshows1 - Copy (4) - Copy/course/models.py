# models.py
from django.db import models

class ExcelData(models.Model):
    data = models.JSONField()

class FormData(models.Model):
    hw_version = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=255)
    sw_version = models.CharField(max_length=255)
    bootloader_version = models.CharField(max_length=255)
    algo_version = models.CharField(max_length=255)
    restbus = models.CharField(max_length=255)
    release_update_mlc = models.CharField(max_length=255)
    doors_test_spec_url = models.URLField(max_length=255)
    doors_viewset = models.CharField(max_length=255)
    jazz_file_name_version = models.CharField(max_length=255)
    test_engineer = models.CharField(max_length=255)
    test_date = models.DateField()
    reviewed_by = models.CharField(max_length=255)
    review_id = models.CharField(max_length=255)
    input1 = models.CharField(max_length=255, blank=True, null=True)  # New field
    input2 = models.CharField(max_length=255, blank=True, null=True)  # New field
