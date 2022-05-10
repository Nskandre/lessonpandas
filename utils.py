from pprint import pprint

from mytest import logs_dict


def all_browsers(logs_dict): # словарь всех браузеров с посещением помесячно
    browsers = {}
    for i in logs_dict:
        if i['Браузер'] in browsers:
            browsers[i['Браузер']][str(i['Дата посещения'].month)] = browsers[i['Браузер']].get(
                str(i['Дата посещения'].month), 0) + 1
        else:
            browsers[i['Браузер']] = {
                str(i['Дата посещения'].month): browsers.get(str(i['Дата посещения'].month), 0) + 1}
    return browsers


def visits_of_browsers(logs_dict): # словарь всех браузеров с посещениями за весь период
    visits_of_browser = {}
    for i in logs_dict:
        visits_of_browser[i['Браузер']] = visits_of_browser.get(i['Браузер'], 0) + 1
    return visits_of_browser


def all_goods(logs_dict): # словарь всех товаров с их покупками помесячно
    goods = {}
    for i in logs_dict:
        for j in i['Купленные товары'].split(','):
            if j in goods:
                goods[j][str(i['Дата посещения'].month)] = goods[j].get(str(i['Дата посещения'].month), 0) + 1
            else:
                goods[j] = {str(i['Дата посещения'].month): goods.get(str(i['Дата посещения'].month), 0) + 1}
    return goods


def buyings(logs_dict): # словарь всех товаров с их покупками за весь период
    buyings_of_goods = {}
    for i in logs_dict:
        for j in i['Купленные товары'].split(','):
            buyings_of_goods[j] = buyings_of_goods.get(j, 0) + 1
    return buyings_of_goods


def mens_choice(logs_dict): # список предпочтений мужчин
    mens_goods = []
    for i in logs_dict:
        if i['Пол'] == 'м':
            for good in i['Купленные товары'].split(','):
                mens_goods.append(good)
    return mens_goods


def women_choice(logs_dict): # список предпочтений женщин
    women_goods = []
    for i in logs_dict:
        if i['Пол'] == 'ж':
            for good in i['Купленные товары'].split(','):
                women_goods.append(good)
    return women_goods


pprint(women_choice(logs_dict))