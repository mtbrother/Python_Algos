"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

from random import random

COUNT = 1
NUMBER = int(random() * 100)

while COUNT <= 10:
    user_num = int(input('Угадайте число: '))
    if user_num < NUMBER:
        print(f'Ваше число меньше. У вас осталось {10 - COUNT} попыток.')
    elif user_num > NUMBER:
        print(f'Ваше число больше. У вас осталось {10 - COUNT} попыток.')
    else:
        print(f'Вы угадали!!! Поздравляю!!!')
        break
    COUNT += 1
print(f'Загаданное число: {NUMBER}')
