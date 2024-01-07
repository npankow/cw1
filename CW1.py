inputarray = input("Введите элементы массива через пробел: ").split()
count = 0
for string in inputarray:
    if len(string) <= 3:
        count += 1

newarray = [None] * count
index = 0
for string in inputarray:
    if len(string) <= 3:
        newarray[index] = string
        index += 1