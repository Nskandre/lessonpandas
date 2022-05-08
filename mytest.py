from collections import Counter
from pprint import pprint

import pandas

read_logs = pandas.read_excel('xlsxtest.xlsx')

logs_dict = read_logs.to_dict(orient='records')

pprint(logs_dict)

browsers, visits_of_browser, goods, buyings_of_goods, raiting_of_browsers, raiting_of_goods = {}, {}, {}, {}, {}, {}
res_browsers, res_goods = {}, {}
mens_goods, women_goods = [], []
mens_popular_goods, women_popular_goods, mens_useless_goods, women_useless_goods = '', '', '', ''

# в цикле словаря logs_dict формируем словарь data_browser - использование браузеров по количеству посещений и по месяцам
# и словарь quantity_of_goods - покупка товаров по количеству и помесяцам
for i in logs_dict:
    visits_of_browser[i['Браузер']] = visits_of_browser.get(i['Браузер'], 0) + 1
    if i['Браузер'] in browsers:
        browsers[i['Браузер']][str(i['Дата посещения'].month)] = browsers[i['Браузер']].get(
            str(i['Дата посещения'].month), 0) + 1
    else:
        browsers[i['Браузер']] = {
            str(i['Дата посещения'].month): browsers.get(str(i['Дата посещения'].month), 0) + 1}

    for j in i['Купленные товары'].split(','):
        buyings_of_goods[j] = buyings_of_goods.get(j, 0) + 1
        if j in goods:
            goods[j][str(i['Дата посещения'].month)] = goods[j].get(
                str(i['Дата посещения'].month), 0) + 1
        else:
            goods[j] = {str(i['Дата посещения'].month): goods.get(str(i['Дата посещения'].month), 0) + 1}

    if i['Пол'] == 'м':
        for good in i['Купленные товары'].split(','):
            mens_goods.append(good)
    else:
        for good in i['Купленные товары'].split(','):
            women_goods.append(good)



sorted_visits_of_browser = sorted(visits_of_browser.values(), reverse=True)
sorted_buyings_of_goods = sorted(buyings_of_goods.values(), reverse=True)


for i in sorted_visits_of_browser:
    for browser in visits_of_browser.keys():
        if visits_of_browser[browser] == i:
            raiting_of_browsers[browser] = i
        if len(raiting_of_browsers) >= 7:
            break


for i in sorted_buyings_of_goods:
    for good in buyings_of_goods.keys():
        if buyings_of_goods[good] == i:
            raiting_of_goods[good] = i
        if len(raiting_of_goods) >= 7:
            break


for browser in raiting_of_browsers.keys():
    res_browsers[browser] = browsers[browser]


for good in raiting_of_goods.keys():
    res_goods[good] = goods[good]


# pprint(browsers)
# pprint(visits_of_browser)
# pprint(goods)
# pprint(buyings_of_goods)
# print(sorted_buyings_of_goods)
# print(sorted_visits_of_browser)
# print(raiting_of_browsers)
# print(len(raiting_of_browsers))
# pprint(raiting_of_goods)
# print(len(raiting_of_goods))
# pprint(res_browsers)
# pprint(res_goods)
pprint(mens_goods)