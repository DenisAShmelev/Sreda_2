from itertools import combinations

max_w = 8300
items = [(1500, 24), (1500, 23), (1500, 22), (1500, 21), (1500, 20), (1500, 19), (1500, 18), (1500, 17), (1500, 16),
         (1200, 15), (1200, 14), (1200, 13), (1200, 12), (1200, 11), (1200, 10), (1200, 9), (1200, 8), (1200, 7),
         (1000, 5), (1000, 4), (1000, 3), (1000, 2), (1000, 1)]  # (11, [(1, 2), (4, 6), (1, 1), (2, 2)])

print(max(filter(lambda x: sum(list(zip(*x))[0]) <= max_w, (v for r in range(1, len(items))
    for v in combinations(filter(lambda x: x[0] <= max_w, items), r))), key=lambda x: sum(list(zip(*x))[1])))

#Разобрать как происходит отбор

# ((1500, 24), (1500, 23), (1500, 22), (1500, 21), (1200, 15), (1200, 14))
# ((1500, 24), (1500, 23), (1500, 22), (1200, 15), (1200, 14), (1200, 13))
