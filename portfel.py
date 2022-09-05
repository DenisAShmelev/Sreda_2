# #!/usr/bin/env python3
# """0-1 knapsack problem: O(n W) in time, space algorithm"""
# from collections import namedtuple
# from functools import lru_cache
#
# Item = namedtuple('Item', 'value weight')
# items = Item(4, 5), Item(3, 4), Item(3, 2), Item(2, 1)
# capacity = 6  # max weight we can put into the knapsack
#
#
# @lru_cache(maxsize=None)  # cache all calls
# def best_value(nitems, weight_limit):
#     if nitems == 0:  # no items
#         return 0  # zero value
#     elif items[nitems - 1].weight > weight_limit:
#         # new item is heavier than the current weight limit
#         return best_value(nitems - 1, weight_limit)  # don't include new item
#     else:
#         return max(  # max of with and without the new item
#             best_value(nitems - 1, weight_limit),  # without
#             best_value(nitems - 1, weight_limit - items[nitems - 1].weight)
#             + items[nitems - 1].value)  # with the new item
#
#
# result = []
# weight_limit = capacity
# for i in reversed(range(len(items))):
#     if best_value(i + 1, weight_limit) > best_value(i, weight_limit):
#         # better with the i-th item
#         result.append(items[i])  # include it in the result
#         weight_limit -= items[i].weight
# print(result)
# print(best_value.cache_info())


# from itertools import combinations
#
# max_w = 15
# items = [(12, 4), (1, 2), (4, 6), (1, 1), (2, 2)]  # (11, [(1, 2), (4, 6), (1, 1), (2, 2)])
#
# print(max(filter(lambda x: sum(list(zip(*x))[0]) <= max_w, (v for r in range(1, len(items))
#     for v in combinations(filter(lambda x: x[0] <= max_w, items), r))), key=lambda x: sum(list(zip(*x))[1])))
#
#
#
# #-----------------------------------------------
#
# from itertools import combinations
# from collections import namedtuple
#
# Good = namedtuple('Good', ['profit', 'weight'])
# goods = [Good(4, 5), Good(3, 4), Good(3, 2), Good(2, 1)]  # sample data
# capacity = 6
#
# print(max(filter(lambda x: sum(list(zip(*x))[0]) <= capacity, (v for r in range(1, len(goods))
#     for v in combinations(filter(lambda x: x[0] <= capacity, goods), r))), key=lambda x: sum(list(zip(*x))[1])))
#
# filter()





#------------------------------------


stuffdict = {'stroiteh_1500': (1500, 100),
             'stroiteh_1500': (1200, 100),
             'stroiteh_1000': (1000, 100),
             'stroiteh_1500': (1500, 100),
             'stroiteh_1200': (1200, 100),
             'stroiteh_1000': (1000, 100),
             'stroiteh_1500': (1500, 100),
             'stroiteh_1200': (1200, 100),
             'stroiteh_1000': (1000, 100),
             'stroiteh_1500': (1500, 100),
             'stroiteh_1200': (1200, 100),
             'stroiteh_1000': (1000, 100),
            }


def get_area_and_value(stuffdict):
    area = [stuffdict[item][0] for item in stuffdict]
    value = [stuffdict[item][1] for item in stuffdict]
    return area, value


def get_memtable(stuffdict, A=10000):
    area, value = get_area_and_value(stuffdict)
    n = len(value)  # находим размеры таблицы

    # создаём таблицу из нулевых значений
    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            # базовый случай
            if i == 0 or a == 0:
                V[i][a] = 0

            # если площадь предмета меньше площади столбца,
            # максимизируем значение суммарной ценности
            elif area[i - 1] <= a:
                V[i][a] = max(value[i - 1] + V[i - 1][a - area[i - 1]], V[i - 1][a])

            # если площадь предмета больше площади столбца,
            # забираем значение ячейки из предыдущей строки
            else:
                V[i][a] = V[i - 1][a]
    return V, area, value


def get_selected_items_list(stuffdict, A=10000):
    V, area, value = get_memtable(stuffdict)
    n = len(value)
    res = V[n][A]  # начинаем с последнего элемента таблицы
    a = A  # начальная площадь - максимальная
    items_list = []  # список площадей и ценностей

    for i in range(n, 0, -1):  # идём в обратном порядке
        if res <= 0:  # условие прерывания - собрали "рюкзак"
            break
        if res == V[i - 1][a]:  # ничего не делаем, двигаемся дальше
            continue
        else:
            # "забираем" предмет
            items_list.append((area[i - 1], value[i - 1]))
            res -= value[i - 1]  # отнимаем значение ценности от общей
            a -= area[i - 1]  # отнимаем площадь от общей

    selected_stuff = []

    # находим ключи исходного словаря - названия предметов
    for search in items_list:
        for key, value in stuffdict.items():
            if value == search:
                selected_stuff.append(key)

    return selected_stuff


stuff = get_selected_items_list(stuffdict)
print(stuff)
totarea = sum([stuffdict[item][0] for item in stuff])
totvalue = sum([stuffdict[item][1] for item in stuff])
print(totarea)
