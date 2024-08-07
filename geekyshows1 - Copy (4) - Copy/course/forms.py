# forms.py
from django import forms
from .models import FormData

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')

class Form2(forms.ModelForm):
    class Meta:
        model = FormData
        fields = [
            'hw_version', 'serial_no', 'sw_version', 'bootloader_version',
            'algo_version', 'restbus', 'release_update_mlc', 'doors_test_spec_url',
            'doors_viewset', 'jazz_file_name_version', 'test_engineer', 'test_date',
            'reviewed_by', 'review_id', 'input1', 'input2'  # Include new fields here
        ]
