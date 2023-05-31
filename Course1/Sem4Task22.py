numbers_1 = int(input("Введите количество элементов первого списка: "))
numbers_2 = int(input("Введите колличество элементов второго списка: "))

list_1 = []
list_2 = []

for i in range(numbers_1):
    list_1.append(int(input("Введите символ первого списка: ")))
print(*list_1)

for i in range(numbers_2):
    list_2.append(int(input("Введите символ второго списка: ")))
print(*list_2)
print()

list_1 = set(list_1)
print(*list_1)
list_2 = set(list_2)
print(*list_2)
list_3 = list_1.intersection(list_2)
print()

list_3 = list(list_3)
list_3.sort
print(*list_3)