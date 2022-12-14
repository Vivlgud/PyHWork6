# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random
list_gen=[random.randint(1,100) for _ in range(200)]

new_list=[]
for i in range(len(list_gen)):
    if i!=list_gen[i]:
        new_list.append(list_gen[i])

res_list=list(zip(list(i for i in range(len(new_list))),new_list))
print (res_list)

# task 6
new_res_list=[]
for i in res_list:
    if (i[0]+i[1])%5==0:
         new_res_list.append((i[0],i[1]))

print(new_res_list)







