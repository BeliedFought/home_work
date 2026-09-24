"""Сумма исходного числа и числа с переставленными второй и третьей цифрами.

Задача: дано четырехзначное число, получить новое число перестановкой второй и
третьей цифр и вывести сумму исходного и нового чисел по образцу.
Пример: 2561 -> 2561+2651=5212.
"""

number = int(input())
thousands = number // 1000
hundreds = number // 100 % 10
tens = number // 10 % 10
ones = number % 10
new_number = thousands * 1000 + tens * 100 + hundreds * 10 + ones
print(str(number) + "+" + str(new_number) + "=" + str(number + new_number))
