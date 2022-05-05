from pprint import pprint

import pandas

read_logs = pandas.read_excel('xlsxtest.xlsx')

logs_dict = read_logs.to_dict(orient='records')

# pprint(logs_dict)

data_browser, browser_rating, quantity_of_goods = {}, {}, {}

# в цикле словаря logs_dict формируем словарь data_browser - использование браузеров по количеству посещений и по месяцам
# и словарь quantity_of_goods - покупка товаров по количеству и помесяцам
for i in logs_dict:
    browser_rating[i['Браузер']] = browser_rating.get(i['Браузер'], 0) + 1
    if i['Браузер'] in data_browser:
        data_browser[i['Браузер']][str(i['Дата посещения'].month)] = data_browser[i['Браузер']].get(str(i['Дата посещения'].month), 0) + 1
    else:
        data_browser[i['Браузер']] = {str(i['Дата посещения'].month): data_browser.get(str(i['Дата посещения'].month), 0) + 1}

    for j in i['Купленные товары'].split(','):
        if j in quantity_of_goods:
            quantity_of_goods[j][str(i['Дата посещения'].month)] = quantity_of_goods[j].get(str(i['Дата посещения'].month), 0) + 1
        else:
            quantity_of_goods[j] = {str(i['Дата посещения'].month): quantity_of_goods.get(str(i['Дата посещения'].month), 0) + 1}



# pprint(data_browser)
# pprint(browser_rating)
# pprint(quantity_of_goods)