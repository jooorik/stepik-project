# put your python code here
en_alph = ''.join([chr(i) for i in range(97, 123)])
en_alph_cap = en_alph.upper()

text = input()
list_txt = text.split()

for i in range(len(list_txt)): #5
    cnt_alph = 0
    for j in range(len(list_txt[i])): #7
        if list_txt[i][j].isalpha():
            cnt_alph += 1 #7
    for j in range(len(list_txt[i])): #1
        word_list = list_txt[i] #tistake!
        if word_list[j].isalpha() and word_list[j] in en_alph: #i
            a = en_alph.find(word_list[j]) #8
            if a + cnt_alph < 26: #15
                word_list_mod = word_list[:j] + word_list[j:].replace(en_alph[a], en_alph[a + cnt_alph], 1)
                list_txt[i] = word_list_mod #tistake!
            else:
                word_list_mod = word_list[:j] + word_list[j:].replace(en_alph[a], en_alph[a + (cnt_alph - 26)], 1)
                list_txt[i] = word_list_mod
        elif word_list[j].isalpha() and word_list[j] in en_alph_cap:
            a = en_alph_cap.find(word_list[j]) #3
            if a + cnt_alph < 26:
                word_list_mod = word_list[:j] + word_list[j:].replace(en_alph_cap[a], en_alph_cap[a + cnt_alph], 1)
                list_txt[i] = word_list_mod
            else:
                word_list_mod = word_list[:j] + word_list[j:].replace(en_alph_cap[a], en_alph_cap[a + (cnt_alph - 26)], 1)
                list_txt[i] = word_list_mod
            
list_txt = ' '.join(list_txt)


print(list_txt)
#print(len(list_txt[0]))





