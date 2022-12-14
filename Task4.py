# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.

list_url=['https://gb.ru/faq', 'https://www.virtualbox.org/wiki', 'https://habr.com/ru/post/349860']


list_temp=list(map(lambda x:x.replace('https://',''),list_url))
list_domen=list(map(lambda s: s[:s.find('/')], [i for i in list_temp]))

print(list_domen)

