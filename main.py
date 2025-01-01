fish_list = ["щука","карась","окунь","таймень","лосось","форель","хариус","кета","горбуша","кижуч"]
spisok = []
f = open('fish.txt','w')
for i in fish_list:
    print(i)
    n = int(input("сколько раз повторить? "))
    for k in range (0,n):
        spisok.append(i)
        f.write(i+'\n')
print(spisok)
f.close() 