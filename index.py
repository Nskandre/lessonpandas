from pprint import pprint

import pandas as pd

# def make_report(log_file_name, report_template_file_name, report_output_file_name):
#    excel_data = pd.read_excel('logs.xlsx', sheet_name='log', engine='openpyxl')
#
#     # Открываем файл шаблона отчета report_template.xlsx
#     wb = load_workbook(filename=report_template_file_name, data_only=True)
#
#     # Выполняем запись данных в объект wb
#     …
#
#     # Сохраняем файл-отчет
#     wb.save(report_output_file_name)