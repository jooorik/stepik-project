from random import * #Подключение библиотеки "random"

def is_val_inp_num(valid): #Создание функции проверки корректности введенного числа
    return valid.isdigit() and 0 < int(valid) < right_border + 1

def inp_right(): #Функция на ввод валидной правой границы
    flag_def = False
    while flag_def == False:
        right_border = right_border = input('Введите правую границу (n) числа для игры (от 1 до n): ')
        if not right_border.isdigit():
            print('Введите целое число!')
        else:
            return right_border


print('Добро пожаловать в числовую угадайку!') #Вывод на экран приветствия и названия игры 

right_border = int(inp_right())
rand_num = randint(1, right_border) #Генерирование случайного числа и сохранение его в переменной
cnt_trying = 0 #Переменная подсчета попыток угадывания
inpt_num = -100 #Переменная вводимая пользователем
yorn = 'д'

while yorn.lower() == 'д' or yorn.lower() == 'да': #Создание цикла на сравнение введенного и сгенерированного числа
    inpt_num = (input(f'Попробуй угадать загаданное число (от 1 до {right_border}): '))
    if is_val_inp_num(inpt_num):
        inpt_num = int(inpt_num)
        if inpt_num > rand_num:
            print('Слишком много, попробуйте еще раз')
            print('\n')
        elif inpt_num < rand_num:
            print('Слишком мало, попробуйте еще раз')
            print('')
        else:
            print('Вы угадали, поздравляем!')
            cnt_trying += 1
            print('Количество попыток, за которое было угадано число:', cnt_trying)
            print()
            yorn = input('Хотите сыграть еще раз? (д/да = да, любой другой символ = нет): ')
            if yorn.lower() == 'д' or yorn.lower() == 'да':
                cnt_trying = 0
                right_border = int(inp_right())
                rand_num = randint(1, right_border) #Генерирование случайного числа и сохранение его в переменной
                continue
        cnt_trying += 1
    else:
        print(f'А может быть все-таки введем целое число от 1 до {right_border}?')
        print()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')