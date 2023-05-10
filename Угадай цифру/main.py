from random import randint
from math import log2, ceil

def guessing_num(num, x, y, count):
    count += 1
    digit = int(input('Введите число: '))
    if digit in range(int(x), int(y)+1):
        if digit > num:
            print('Слишком много, попробуй еще раз')
            guessing_num(num, x, y, count)
        elif digit < num:
            print('Слишком мало, попробуй еще раз')
            guessing_num(num, x, y, count)
        elif digit == num:
            print('Поздравляю вы угадали число')
            print('Ваше кол-во попыток:', count,)
            repeat_game = input('Хотите еще раз? да\нет\n')
            if repeat_game == 'да':
                start_of_game()
            else:
                print('Заходите еще, когда будет время')
    else:
        print('Ошибка, вы должны ввести число больше', x, 'и меньше', y)
        guessing_num(num, x, y, count)

def input_x():
    x = input(('Введите правую границу диапазона:\n'))
    if x.isdigit():
        return x
    else:
        print('Ошибка. Возможно вы ввели не число')
        input_x()

def input_y():
    y = input(('Хорошо,теперь введите левую границу диапазона:\n'))
    if y.isdigit():
        return y
    else:
        print('Ошибка. Возможно вы ввели не число')
        input_y()

def start_of_game():
    count = 0
    name = input('Итак, для начала игры мне нужно знать как вас зовут: \n')
    print('Приятно познакомиться,', name)
    print('Правила игры крайне просты: вам необходимо угадать число из вашего диапазона')
    x = input_x()
    y = input_y()
    if int(x) > int(y):
        x, y = y, x
    num = randint(int(x), int(y))
    print('Число загадано в проммежутке от', x, 'до', y, 'вкючительно')
    guessing_num(num, x, y, count)


print('\t\t\tИгра "Числовая угадайка"')
start = input(('Хотите проверить свою интуицию? да/нет\n'))
if start == 'да':
    start_of_game()
else:
    print('Жалко конечно, но вы всегда можете поиграть запустив программу')