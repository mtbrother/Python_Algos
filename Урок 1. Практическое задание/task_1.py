"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""
DIGIT = int(input('Введите трехзначное число:'))
if DIGIT > 999 or DIGIT < 100 or DIGIT == 0 or DIGIT == str:
    print('Неверный ввод, попробуйте в другой раз!')
else:
    DIGIT_ONE = DIGIT // 100
    DIGIT_TWO = (DIGIT - DIGIT_ONE * 100) // 10
    DIGIT_THREE = (DIGIT % ((DIGIT_ONE * 100) + (DIGIT_TWO * 10)))
    print(DIGIT_ONE + DIGIT_TWO + DIGIT_THREE)
    print(DIGIT_ONE * DIGIT_TWO * DIGIT_THREE)
