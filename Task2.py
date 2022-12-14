# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
new_list=[random.randint(1,10) for _ in range(10)]
print (new_list)
rev_new_list=new_list[::-1]

list_for_mult=list(zip(new_list,rev_new_list ))
list_for_mult=list_for_mult[:round(len(list_for_mult)/2+0.1)]

result=[]
for i,j in list_for_mult:
    result.append(i*j)

print(result)






