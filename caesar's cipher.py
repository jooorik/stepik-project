print('Приветствую! Программа "Шифр Цезаря"')


text = input('Введите текст который необходимо преобразовать: ')
direction = input('Укажите направление (шифрование или дешифрование - ш/д): ')
alph = input('Укажите язык вводимого собщения (английский/русский - а/р(кириллица)): ')
step = int(input('Укажите шаг сдвига (со сдвигом вправо): '))

en_alph = ''.join([chr(i) for i in range(97, 123)])
en_alph_cap = en_alph.upper()
ru_alph = ''.join([chr(i) for i in range(1072, 1104)])
ru_alph_cap = ru_alph.upper()

def cipher_en(step, text):
    cipher_txt = ''
    for i in range(len(text)):
        if text[i] in en_alph:
            ind = en_alph.find(text[i]) + step
            if ind > 25:
                ind -= 26
                cipher_txt += en_alph[ind]
            elif ind <= 25:
                cipher_txt += en_alph[ind]
        elif text[i] in en_alph_cap:
            ind = en_alph_cap.find(text[i]) + step
            if ind > 25:
                ind -= 26
                cipher_txt += en_alph_cap[ind]
            elif ind <= 25:
                cipher_txt += en_alph_cap[ind]
        else:
            cipher_txt += text[i]
    return cipher_txt  

def cipher_ru(step, text):
    cipher_txt = ''
    for i in range(len(text)):
        if text[i] in ru_alph:
            ind = ru_alph.find(text[i]) + step
            if ind > 31:
                ind -= 32
                cipher_txt += ru_alph[ind]
            elif ind <= 31:
                cipher_txt += ru_alph[ind]
        elif text[i] in ru_alph_cap:
            ind = ru_alph_cap.find(text[i]) + step
            if ind > 31:
                ind -= 32
                cipher_txt += ru_alph_cap[ind]
            elif ind <= 31:
                cipher_txt += ru_alph_cap[ind]
        else:
            cipher_txt += text[i]
    return cipher_txt  

def dciper_en(step, text):
    dcipher_txt = ''
    for i in range(len(text)):
        if text[i] in en_alph:
            ind = en_alph.find(text[i]) - step
            if ind < 0:
                ind += 26
                dcipher_txt += en_alph[ind]
            elif ind >= 0:
                dcipher_txt += en_alph[ind]
        elif text[i] in en_alph_cap:
            ind = en_alph_cap.find(text[i]) - step
            if ind < 0:
                ind += 26
                dcipher_txt += en_alph_cap[ind]
            elif ind >= 0:
                dcipher_txt += en_alph_cap[ind]
        else:
            dcipher_txt += text[i]
    return dcipher_txt  

def dciper_ru(step, text):
    dcipher_txt = ''
    for i in range(len(text)):
        if text[i] in ru_alph:
            ind = ru_alph.find(text[i]) - step
            if ind < 0:
                ind += 32
                dcipher_txt += ru_alph[ind]
            elif ind >= 0:
                dcipher_txt += ru_alph[ind]
        elif text[i] in ru_alph_cap:
            ind = ru_alph_cap.find(text[i]) - step
            if ind < 0:
                ind += 32
                dcipher_txt += ru_alph_cap[ind]
            elif ind >= 0:
                dcipher_txt += ru_alph_cap[ind]
        else:
            dcipher_txt += text[i]
    return dcipher_txt  

def output(alph, direction):
    if alph == 'а' and direction == 'ш':
        return cipher_en(step, text)
    elif alph == 'р' and direction == 'ш':
        return cipher_ru(step, text)
    elif alph == 'а' and direction == 'д':
        return dciper_en(step,text)
    elif alph == 'р' and direction == 'д':
        return dciper_ru(step,text)
    else:
        return 'Ошибка ввода!'

print(output(alph, direction))