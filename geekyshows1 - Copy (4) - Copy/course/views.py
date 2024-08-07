# views.py
from django.shortcuts import render, redirect
from .forms import ExcelUploadForm, Form2
from .models import ExcelData, FormData
import pandas as pd
import re

def import_excel(request):
    form = ExcelUploadForm()
    latest_form2_data = FormData.objects.last()
    if latest_form2_data:
        form2 = Form2(instance=latest_form2_data)
    else:
        form2 = Form2()

    if request.method == 'POST':
        if 'excel_file' in request.FILES:
            form = ExcelUploadForm(request.POST, request.FILES)
            if form.is_valid():
                excel_file = request.FILES['excel_file']
                df = pd.read_excel(excel_file)
                
                id_column = next((col for col in df.columns if 'ID' in col), None)
                expected_result_column = next((col for col in df.columns if 'ExpectedResult' in col), None)
                test_spec_column = next((col for col in df.columns if 'System_Integration_Test_Spec' in col), None)
                test_result_column = next((col for col in df.columns if 'TestStatus' in col), None)
                
                if test_spec_column:
                    def remove_number_patterns(text):
                        return re.sub(r'\b\d+(\.\d+){2,}\b', '', text)
                    
                    df[test_spec_column] = df[test_spec_column].apply(
                        lambda x: remove_number_patterns(x) if isinstance(x, str) else x
                    )

                for column in df.columns:
                    if column not in [expected_result_column, test_result_column]:
                        df[column] = df[column].apply(lambda x: re.split(r'\.\D|\n|\t', x)[0] if isinstance(x, str) else x)
                    
                column_names = df.columns.tolist()
                column_values = {column: df[column].unique().tolist() for column in column_names}

                filters = {column: request.POST.get(column, '') for column in column_names}
                filters = {k: v for k, v in filters.items() if v}
                for column, value in filters.items():
                    df = df[df[column] == value]

                detailed_rows = []
                for _, row in df.iterrows():
                    id_value = row[id_column] if id_column else 'N/A'
                    test_case_name = row[test_spec_column] if test_spec_column else ''
                    test_result = row[test_result_column] if test_result_column else ''
                    numeric_part = re.search(r'\d+$', id_value).group() if id_column and isinstance(id_value, str) else ''
                    expected_result = row[expected_result_column] if expected_result_column else 'N/A'
                    
                    if isinstance(expected_result, str):
                        expected_result = re.sub(r'^\.', '', expected_result)
                        expected_result_lines = expected_result.split('\n')
                    else:
                        expected_result_lines = []

                    detailed_row = {
                        'id': id_value,
                        'test_case_name': test_case_name,
                        'test_result': test_result,
                        'numeric_part': numeric_part,
                        'expected_result_lines': expected_result_lines,
                    }
                    detailed_rows.append(detailed_row)

                columns_to_remove = ['Importance', 'TestGroup', 'Remark','CarryOver','SafetyRelevant']
                df_display = df.drop(columns=[col for col in df.columns if any(keyword in col for keyword in columns_to_remove)], errors='ignore')

                if expected_result_column:
                    df_display = df_display.drop(columns=[expected_result_column], errors='ignore')

                data_html = df_display.to_html(escape=False, index=False)

                try:
                    ExcelData.objects.create(data=data_html)

                    return render(request, 'import_excel.html', {
                        'form': form,
                        'form2': form2,
                        'column_names': column_names,
                        'column_values': column_values,
                        'filtered_data': data_html,
                        'detailed_rows': detailed_rows,
                        'form2_data': FormData.objects.all(),
                    })
                except ValueError:
                    error_message = "Error: Invalid JSON data."
                    return render(request, 'import_excel.html', {'form': form, 'error_message': error_message})

        elif 'submit-form2' in request.POST:
            form2 = Form2(request.POST)
            if form2.is_valid():
                FormData.objects.all().delete()  
                form2.save() 
                return redirect('import_excel')

    return render(request, 'import_excel.html', {
        'form': form,
        'form2': form2,
        'form2_data': FormData.objects.all(),
    })