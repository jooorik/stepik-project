import random

word_list = ['виселица', "ложка", "вилка", "Бисер", "Всадник", "Закоренеть", "Книжник",  "Оточить", "Реформа",
 "Санки", "Сжигать", "Состояться", "Эспадрон"]

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
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
    return stages[tries]

def play(word):
   word_completion = ('_' + ' ') * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
   guessed = False                    # сигнальная метка
   guessed_letters = []               # список уже названных букв
   guessed_words = []                 # список уже названных слов
   tries = 6                          # количество попыток

   print('Давайте играть в угадайку слов!')
   print(display_hangman(tries))
   print(word_completion)
   
   while tries > 0 and guessed:
        inp = input('Введите слово целиком или букву: ').upper()
        if len(inp) == 1 and inp not in guessed_letters and inp not in word: #введённой буквы в слове нет 
            guessed_letters.append(inp)
            tries -= 1
            print(display_hangman(tries))
        elif len(inp) == 1 and inp not in guessed_letters and inp in word: #введённая буква в слове есть
            guessed_letters.append(inp)
            for i in range(len(word)):
                if inp == word[i]:
                    word_completion = word_completion[:i*2] + word[i] + word_completion [i*2+1:]
            if ''.join([word_completion[i] for i in range(0, len(word_completion), 2)]).upper() == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                guessed = True
        elif len(inp) > 1 and inp == word: #введённое и загаданное слова совпадают
            print('Поздравляем, вы угадали слово! Вы победили!')
            guessed = True
        elif len(inp) > 1 and inp not in guessed_words:
            guessed_words.append(inp)
            tries -= 1
            print(display_hangman(tries))
        elif inp in guessed_letters or inp in guessed_words: #введённый текст введён повторно
            print('Вы уже это вводили!')
        if tries == 0:
            print('Загаданное слово: ' + word)
        if guessed == False:
            print(word_completion)
      
def run():
    played = 'д'
    while played == 'д':
        word = get_word()
        play(word)
        played = input('Хотите сыграть еще раз?(да - д) ')
    print('Спасибо за игру, приходите еще!')

run()