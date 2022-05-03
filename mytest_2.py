from pprint import pprint

logs_dict = [{'IP-адрес': '188.32.242.xxx',
              'Браузер': 'Android Browser',
              'Версия браузера': 'Android Browser 9',
              'Возраст': 67,
              'Время на сайте': '00:08:16',
              'Дата посещения': '2020-03-24 00:00:00',
              'Купленные товары': 'Сменный ремешок для Xiaomi Mi Band 4 и Mi Band 3 '
                                  'Черный,Силиконовый ремешок для фитнес-браслета Xiaomi '
                                  'Mi Band 3 ,ArtSpace Набор обложек для дневников и '
                                  'тетрадей 208х346 мм',
              'Пол': 'м'},
             {'IP-адрес': '95.220.45.xxx',
              'Браузер': 'Opera',
              'Версия браузера': 'Android Browser 10',
              'Возраст': 66,
              'Время на сайте': '00:08:50',
              'Дата посещения': '2020-07-09 00:00:00',
              'Купленные товары': 'Защитное стекло FULL GLUE стекло для Apple iPhone 11 '
                                  ',Защитное стекло 5D для Samsung Galaxy A31 ,Berlingo '
                                  'Мешок для обуви Challenge (MS09239) черный',
              'Пол': 'м'},
             {'IP-адрес': '188.32.242.xxx',
              'Браузер': 'Android Browser',
              'Версия браузера': 'Android Browser 9',
              'Возраст': 67,
              'Время на сайте': '00:08:16',
              'Дата посещения': '2020-03-24 00:00:00',
              'Купленные товары': 'Сменный ремешок для Xiaomi Mi Band 4 и Mi Band 3 '
                                  'Черный,Силиконовый ремешок для фитнес-браслета Xiaomi '
                                  'Mi Band 3 ,ArtSpace Набор обложек для дневников и '
                                  'тетрадей 208х346 мм',
              'Пол': 'м'}]

data_browser = {}

for i in logs_dict:
    data_browser.setdefault(i['Браузер'], {i['Дата посещения']: data_browser.get(i['Дата посещения'], 0) + 1})

print(data_browser)