from pprint import pprint

import pandas

read_logs = pandas.read_excel('xlsxtest.xlsx')

logs_dict = read_logs.to_dict(orient='records')

data_browser = {}

test_date = logs_dict[0]['Дата посещения']


# for i in logs_dict:
#     data_browser[i.get('Браузер')]: {(i.get('Дата посещения').month): }
#     print(i.get('Браузер'))


pprint(logs_dict)
# print(logs_dict[0]['Дата посещения'])
# print(test_date.month, type(test_date))