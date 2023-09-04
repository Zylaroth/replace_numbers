# Получаем от пользователя число
n = int(input("Введите число: "))

# Получаем от пользователя строку
string_to_replace = input("Введите строку: ")

# Создаем список из натуральных чисел
numbers = list(range(1, n + 1))

# Заменяем нечётные числа на введенную строку
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] = string_to_replace

# Выводим список
print(numbers)