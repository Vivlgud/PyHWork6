# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list_for_check=["qwe", "asd", "zxc", "qwe", "ertqwe"]
find_text='qwe'

find_index=list(map(lambda s:s.find(find_text)!=-1,list_for_check))

count=0
for i in range(len(find_index)):
    if find_index[i]==True:
        count+=1
    if count==2:
        print(i)
        break
   
  

