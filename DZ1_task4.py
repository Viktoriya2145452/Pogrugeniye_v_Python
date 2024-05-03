# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать "больше" или "меньше" после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

n = randint(LOWER_LIMIT, UPPER_LIMIT)
hidden_n = -1
attempts = 10

while hidden_n != n :
    hidden_n = int(input("Угадайте число: "))
    if hidden_n < n:
        print(f"Загаданное число больше")
    elif hidden_n > n:
        print(f"Загаданное число меньше")
    else:
        print(f"Угадали!")
    attempts -= 1
    if attempts == 0:
        print(f"Попытки закончились")
        break