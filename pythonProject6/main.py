from random import choice


def repeat():
    start = input('Хотите еще раз? да/нет\n')
    if start == 'да':
        start_of_game()
    else:
        print('Спасибо за игру)')

def display_hangman(count):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[count]

def input_symbol():
    simbol = input('Введите букву:\n')
    while not simbol.isalpha():
        print('Ошибка, необходимо ввести букву')
        input_symbol()
    else:
        return simbol

def start_of_game():
    words_for_game = ["история", "везение", "щепка", "готика", "биение", "больница", "брак", "орангутанг", "смекалка",
                      "ремень", "тубус", "сорняк", "сессия", "лесник", "вестибюль", "крематорий", "пена", "беляш",
                      "одноклассник", "глушитель", "беда", "заказчик", "шахматист", "номер", "око", "сноп",
                      "заработок", "таджик", "интерес", "фея", "меч", "тарелка", "пингвин", "полнота", "пустота",
                      "пир", "партер", "шкаф", "химия", "парфюм", "срок", "конкурс", "судьба", "внучка", "комета",
                      "синяк", "поведение", "квартира", "цикл", "парус", "тоник", "пластырь", "наездник", "вид",
                      "состав", "еженедельник", "простота", "мелочь", "шарманка", "лыжня", "курс", "хулиганство",
                      "лисица", "столица", "базар", "зевок", "всадник", "проспект", "ель", "муравейник", "стан",
                      "головастик", "рысца", "оковы", "хребет", "телёнок", "аттестат", "храм", "сафари", "принтер",
                      "шах", "диапазон", "нежить", "скорпион", "раствор", "гражданка", "тротуар", "супруг", "чистка",
                      "ремонт", "певец", "виноград", "список", "факс", "вена", "кадр", "чистота", "анкета", "кекс", "жаба"]
    the_hidden_word = choice(words_for_game)
    print('Слово загадано, можно начинать')
    print('_'*len(the_hidden_word))
    count = 6
    letter = input_symbol()
    word = ''
    for i in range(len(the_hidden_word)):
        word += '_ '
    while True:
        if letter in the_hidden_word:
            for i in range(len(the_hidden_word)):
                if the_hidden_word[i] == letter:
                    word = word.split(' ')
                    word[i] = the_hidden_word[i]
                    word = ' '.join(word)
            if '_' not in word:
                print('Вы победили!!!')
                print('Загаданное слово:', the_hidden_word)
                repeat()
                break
            print(word)
            letter = input_symbol()
        else:
            print('Такой буквы нет, попробуй еще раз')
            count -= 1
            print(display_hangman(count))
            letter = input_symbol()
        if  count == 0:
            print(display_hangman(count))
            print('Вы проиграли!!!')
            repeat()
            break

print('\t\t\tИгра: Висилица')
print('Правила просты: я загадываю слово, а ты отгадываешь')
print('Кол-во попыток ограничено, так как за каждую неправильную букву будет дорисовываться часть тела к висилице')
print('Всего можно допустить 6 ошибок')
start = input('Хочешь сыграть? да/нет\n')
if start == 'да':
    start_of_game()
elif start == 'нет':
    print('Ну, как хочешь')
