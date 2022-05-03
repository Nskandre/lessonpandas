from collections import Counter, defaultdict

sales_log = [{'user': 'Маша', 'item': 'Телескоп'},
             {'user': 'Юля', 'item': 'Айфон'},
             {'user': 'Иван', 'item': 'Ноутбук'},
             {'user': 'Сергей', 'item': 'Браслет'},
             {'user': 'Инна', 'item': 'Айфон'},
             {'user': 'Ольга', 'item': 'Айфон'},
             {'user': 'Дмитрий', 'item': 'Браслет'}, ]

sales_dict = defaultdict(int)


for element in sales_log:
    # Добавляем элемент в словарь sales_dict
    # element['item'] - название товара
    # Если ключа с таким названием в sales_dict нет, то будет значение 0,
    # таким образом мы просто увеличим его на 1
    sales_dict[element['item']] += 1

most_common_sales = Counter(sales_dict).most_common(1)

print(f'Самый популярный товар: {most_common_sales[0][0]}. Количество продаж: {most_common_sales[0][1]}')