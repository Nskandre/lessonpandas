from pprint import pprint

import pandas

read_logs = pandas.read_excel('xlsxtest.xlsx')

logs_dict = read_logs.to_dict(orient='records')

# pprint(logs_dict)

data_browser, browser_rating = {}, {}

# create dict 'data_browser'
for i in logs_dict:
    browser_rating[i['Браузер']] = browser_rating.get(i['Браузер'], 0) + 1
    if i['Браузер'] in data_browser:
        data_browser[i['Браузер']][str(i['Дата посещения'].month)] = data_browser[i['Браузер']].get(str(i['Дата посещения'].month), 0) + 1
    else:
        data_browser[i['Браузер']] = {str(i['Дата посещения'].month): data_browser.get(str(i['Дата посещения'].month), 0) + 1}


pprint(data_browser)
pprint(browser_rating)