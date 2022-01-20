import random

spec_smb = '!#$%&*+-=?@^_.'

print('Генератор паролей!')
print('Позволяет создавать пароли с заданными пользователем параметрами: длина и наличие специальных символов')

len_pas = (input('Введите длину пароля(от 8 до 16): '))
print('Укажите необходимые символы в пароле, используя "+" и "-". После каждого ввода параметра нажмите Enter: ')
dt, smb = input('Цифры? '), input('Спец символы? ')
len_pas, dt, smb

def valid_len_pas(len_pas):
    if len_pas.isdigit() and 7 < int(len_pas) < 17:
        return True
    return False

def restart():
    restart = input('Сгенерировать пароль еще раз?(да/нет)')
    if restart.lower() == 'да':
        return (pas(len_pas))

def pas(len_pas):
    if not valid_len_pas(len_pas):
        return 'Неверная длина пароля!'
    password = ''
    if dt == '+' and smb == '+':
        for i in range(int(len_pas)):
            rand = random.randint(0, 100)
            if rand < 26:
                char = random.randint(65, 90)
                password += chr(char)
            elif 25 < rand < 51:
                char = random.randint(97, 122)
                password += chr(char)
            elif 50 < rand < 76:
                char = random.randint(48, 57)
                password += chr(char)
            else:
                password += random.choice(spec_smb)
    elif dt == '+':
        for i in range(int(len_pas)):
            rand = random.randint(0, 100)
            if rand < 34:
                char = random.randint(65, 90)
                password += chr(char)
            elif 33 < rand < 67:
                char = random.randint(97, 122)
                password += chr(char)
            else:
                char = random.randint(48, 57)
                password += chr(char)
    elif smb == '+':
        for i in range(int(len_pas)):
            rand = random.randint(0, 100)
            if rand < 34:
                char = random.randint(65, 90)
                password += chr(char)
            elif 33 < rand < 67:
                char = random.randint(97, 122)
                password += chr(char)
            else:
                password += random.choice(spec_smb)
    else:
        for i in range(int(len_pas)):
            rand = random.randint(0, 100)
            if rand < 51:
                char = random.randint(65, 90)
                password += chr(char)
            else:
                char = random.randint(97, 122)
                password += chr(char)
    return password

print(pas(len_pas))