from openpyxl import load_workbook

wb = load_workbook(filename = 'logs.xlsx')

sheet_br = wb['log']

print(sheet_br['Браузер'].column)