import random


print('Генератор паролей!')
quantity_pas = input('Какое количество паролей вам необходимо? ')
length_pas = input('Введите длину пароля: ')
digits_pas = input('Использовать ли цифры в пароле?(да/нет) ')
low_letters_pas = input('Использовать строчные буквы в пароле?(да/нет) ')
up_letters_pas = input('Использовать прописные буквы в пароле?(да/нет) ')
spec_sb_pas = input('Использовать спец символы в пароле?(да/нет) ')
exception_amb_pas = input('Исключить неоднозначные символы?(да/нет) ')

chars = ''
spec_smb = '!#$%&*+-=?@^_.'
amb_pas = 'il1Lo0O'


if digits_pas.lower() == 'да':
    for i in range(48, 58):
        chars += chr(i)
if low_letters_pas.lower() == 'да':
    for i in range(97, 123):
        chars += chr(i)
if up_letters_pas.lower() == 'да':
    for i in range(65, 91):
        chars += chr(i)
if spec_sb_pas.lower() == 'да':
    for c in spec_smb:
        chars += c
if exception_amb_pas.lower() == 'да':
    for c in amb_pas:
        if c in chars:
            chars.replace(c, '')

def generate_password(length, chars):
    password = ''
    for _ in range(int(length)):
        password += random.choice(chars)
    return password

for i in range(int(quantity_pas)):
    print(generate_password(length_pas, chars))