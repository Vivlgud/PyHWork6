# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# def degree(x:int):
#     return -3**x

# print(degree(5))
# n=int
# for i in range(n)

n=int(input("Введите число N членов последовательности: "))
list=[]
list=[(-3)**x for x in range(n)]

print(list)