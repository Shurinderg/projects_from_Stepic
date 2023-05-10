def corect_text(language, text):
    for i in text:
        if i.isalpha():
            if language == 1 and i.lower() in en_lower_alphabet or language == 2 and i.lower() in ru_lower_alphabet:
                return False
    return True

def work_with_text(direction, language, step, text):
    true_text = ''
    result = ''
    if language == 1:
        abc = ru_lower_alphabet
        ABC = ru_upper_alphabet
        n = 32
    elif language == 2:
        abc = en_lower_alphabet
        ABC = en_upper_alphabet
        n = 26
    for i in text:
        if i == 'ё':
            true_text += 'е'
        else:
            true_text += i

    for i in range(len(true_text)):
        if direction == 1:
            if true_text[i].isalpha():
                if true_text[i].islower():
                    result += abc[(abc.find(true_text[i]) + step) % n]
                elif true_text[i].isupper():
                    result += ABC[(ABC.find(true_text[i]) + step) % n]
            else:
                result += true_text[i]
        if direction == 2:
            if true_text[i].isalpha():
                if true_text[i].islower():
                    result += abc[(abc.find(true_text[i]) - step) % n]
                elif true_text[i].isupper():
                    result += ABC[(ABC.find(true_text[i]) - step) % n]
            else:
                result += true_text[i]
    return result


en_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
en_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
ru_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print('\n\n\n"Шифр Цезаря"\n')
while True:
    direction = int(input('Выбирите вариант работы:\n1)Зашифровать\n2)Расшифровать\n'))
    if direction not in [1, 2]:
        print('Ошибка ввода варианта работы, введите 1 или 2\n')
    else:
        break
while True:
    language = int(input('Язык текста:\n1)Русский\n2)Английский\n'))
    if language not in [1, 2]:
        print('Ошибка ввода языка текста, введите 1 или 2\n')
    else:
        break
while True:
    step = input('Введите шаг сдвига:\n')
    if not step.isdigit():
        print('Ошибка, введите число\n')
    else:
        step = int(step)
        break
while True:
    text = input('Введите текст:\n')
    if not corect_text(language, text):
        print('Ошибка введите текст на том языке, который выбрали для работы\n')
    else:
        break
print(work_with_text(direction, language, step, text))