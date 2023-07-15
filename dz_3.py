# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.
numbers = 5,7,5,3,5,7,4,2,3

repeat_elements = set()
for i in numbers:
    if numbers.count(i) > 1:
        repeat_elements.add(i)
print(numbers)    
print(repeat_elements)

# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из 
# документации к языку.
text = "Олень - северное животное. В летнее время оленям в тайге жарко, а в горах даже в июле холодно. "\
"Олень как бы создан для северных просторов, жёсткого ветра и длинных морозных ночей. "\
"Олень легко бежит вперёд по тайге, подминает под себя кусты и переплывает быстрые реки"

diction = {}
text_split = text.lower().split()

for i in text_split:
    clear = i.strip(",.-!")
    if clear not in diction:
        diction[clear] = 1
    else: diction[clear] += 1

res = dict(sorted(diction.items(), reverse = True))
print(res)
print(diction)

# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.

list = {'food': 3, 'maps': 1, 'tent': 2, 'bags': 2}
max_weight = 5

def backpack(list, max_weight):
    second_list = []
    for item, weight in list.items():
        if weight <= max_weight:
            second_list.append(item)
            max_weight -= weight
    return second_list

print(backpack(list, max_weight)) 