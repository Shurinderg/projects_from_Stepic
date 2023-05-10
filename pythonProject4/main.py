from random import sample

def symbols_for_password(digit, spec, l_or_u):
    numbers = [chr(i) for i in range(48, 57)]
    spec_symbols = [chr(i) for i in range(33, 48)]
    abc = [chr(i) for i in range(97, 122)]
    ABC = [chr(i) for i in range(65, 91)]
    symbols = []
    if digit == 'да':
        symbols += numbers
    if spec == 'да':
        symbols += spec_symbols
    if l_or_u == 1:
        symbols += ABC
    if l_or_u == 2:
        symbols += abc
    if l_or_u == 3:
        symbols += ABC
        symbols += abc
    return symbols


def generade_password(len, digit, spec, l_or_u):
    password = sample(symbols_for_password(digit, spec, l_or_u), len)
    return password



print('Вас приветствует генератор паролей')
len_of_password = int(input('Из скольки символов должен состоять пароль? '))
digit_in_password = input('Должены ли в пароле быть цифры? да/нет ')
special_symbols = input('Должен ли пароль содержать спец. символы? да/нет ')
lower_or_upper = int(input('Пароль должен содержать: \n1)только заглавные буквы\n2)только строчные буквы\n3)и заглавные и строчные\n'))

print('Ваш пароль:\t',*generade_password(len_of_password, digit_in_password, special_symbols, lower_or_upper))