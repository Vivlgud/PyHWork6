# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]


import random
list_gen=[random.randint(1,100) for _ in range(200)]

new_list=[]
for i in range(len(list_gen)):
    if i!=list_gen[i]:
        new_list.append(list_gen[i])

res_list=list(zip(list(i for i in range(len(new_list))),new_list))


print (res_list)

