# file open,write and close. 
file = open('example.txt', 'w') 
file.write("Hello World!\nHi world")  # Записывает строку в файл 
file.close() 






#file open,write "lines First" and close.
file = open('example.txt', 'w') 
file.write("Hello World!\nHi world")  # Записывает строку в файл 
lines = ["\nFirst line\n", "Second line\n"]
file.writelines(lines) 
file.close()  





# file open read information.
file = open('example.txt', 'w') 
file.write("Hello World!\nHi world")  # Записывает строку в файл 
lines = ["\nFirst line\n", "Second line\n"]
file.writelines(lines) 
file.close()
file = open('example.txt', 'r') 
content = file.read()  # Читает весь файл   
file.close()
print(content) 





# This file print information and my name!
file = open('example.txt', 'w') 
file.write("Hello World!\nHi world")  # Записывает строку в файл 
lines = ["\nFirst line\n", "Second line\n"]
file.writelines(lines) 
file.close()
file = open('example.txt', 'r') 
content = file.read()  # Читает весь файл   
file.close()
print(content)
file = open('example.txt', 'a') 
file.write("My name is Sasha.\nI am 11 years old.")
file.close()
file = open('example.txt', 'r') 
content = file.read()  # Читает весь файл   
print(content)
file.close()











# Programm for password.
file = open('my_password', 'r') 
for line in file:
    pass 
file.close() 
while True:
    key_password = input("Enter password ") 
    if key_password == line:
        print("Access granted")
        break
    else:
        print("Access not granted")





#password
import hashlib
salt = 'Ваша соль'.encode()
file = open("my_hash","r")
for hash in file:
    pass 
file.close()
print(hash)

s = '0123456789qwertyuiopasdfghjklzxcvbnm' 
#s = "0123456789"
cont = True
for c1 in s:
    if cont:
        for c2 in s:
            if cont:
                for c3 in s:
                    if cont:
                        for c4 in s:
                            password = (c4 + c3 + c2 + c1).encode()
                            dk = hashlib.pbkdf2_hmac('sha512', password, salt, 10)

                            print(password)
                            if hash == dk.hex():
                                cont = False
                                print("пароль совпал",password)
                                print(password.decode())
                                break
print("перебор закончен")






#second password prgramm
import hashlib
salt = 'Ваша соль'.encode()
file = open("my_hash","r")
for hash in file:
    pass 
file.close()
print(hash)

s = '0123456789qwertyuiopasdfghjklzxcvbnm' 
#s = "0123456789"
cont = True
for c1 in s:
    if cont:
        for c2 in s:
            if cont:
                for c3 in s:
                    if cont:
                        for c4 in s:
                            if cont:
                                for c5 in s:
                                    if cont:
                                        for c6 in s:
                                            password = (c6 + c5 + c4 + c3 + c2 + c1).encode()
                                            dk = hashlib.pbkdf2_hmac('sha512', password, salt, 10)

                                            print(password)
                                            if hash == dk.hex():
                                                cont = False
                                                print("пароль совпал",password)
                                                print(password.decode())
                                                break
print("перебор закончен")





#This programm the best.

#We don't need file.close() we are need with open('example.txt', 'a') as file:
#with open('example.txt', 'a') as file:
    #file.write("Hello, World!")  
file = open('example.txt', 'w') 
file.write("Hello World!\nHi world")  # Записывает строку в файл 
lines = ["\nFirst line\n", "Second line\n"]
file.writelines(lines) 
file = open('example.txt', 'r') 
content = file.read()  # Читает весь файл   
print(content)
file = open('example.txt', 'a') 
file.write("My name is Sasha.\nI am 11 years old.")
file = open('example.txt', 'r') 
content = file.read()  # Читает весь файл   
print(content)
file.close()
with open('example.txt', 'a') as file:
    file.write("Hello, World!")

# Programm for password.
file = open('my_password', 'r') 
for line in file:
    pass 
file.close() 
while True:
    key_password = input("Enter password ") 
    if key_password == line:
        print("Access granted")
        break
    else:
        print("Access not granted")
#password
import hashlib
salt = 'Ваша соль'.encode()
file = open("my_hash","r")
for hash in file:
    pass 
file.close()
print(hash)

s = '0123456789qwertyuiopasdfghjklzxcvbnm' 
#s = "0123456789"
cont = True
for c1 in s:
    if cont:
        for c2 in s:
            if cont:
                for c3 in s:
                    if cont:
                        for c4 in s:
                            password = (c4 + c3 + c2 + c1).encode()
                            dk = hashlib.pbkdf2_hmac('sha512', password, salt, 10)

                            print(password)
                            if hash == dk.hex():
                                cont = False
                                print("пароль совпал",password)
                                print(password.decode())
                                break
print("перебор закончен")






#продвинутая программа перебора пароля

import itertools
import string
import time


def brute_force_password(target_password,n):
    # Определяем символы, которые будем использовать
    characters = string.ascii_letters + string.digits + string.punctuation

    # Начинаем с длины 1 до 6 символов
    for length in range(1, n + 1):
        for guess in itertools.product(characters, repeat=length):
            guess_password = ''.join(guess)
            print(f"Пробуем: {guess_password}")

            if guess_password == target_password:
                print(f"Пароль найден: {guess_password}")
                return

    print("Пароль не найден.")


if __name__ == "__main__":
    # Установите целевой пароль здесь (например, 'abc123')
    target_password = input("Введите целевой пароль: ")
    n = int(input("сколько символов максимально? "))

    start_time = time.time()
    brute_force_password(target_password,n)
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд.")
    print(string.ascii_letters)
    print(string.digits)
    print(string.punctuation)









import itertools
import string
import time


def brute_force_password(target_password,n,characters):
    # Определяем символы, которые будем использовать

    # Начинаем с длины 1 до 6 символов
    for length in range(1, n + 1):
        for guess in itertools.product(characters, repeat = length):
            guess_password = ''.join(guess)
            print(f"Пробуем: {guess_password}")

            if guess_password == target_password:
                print(f"Пароль найден: {guess_password}")
                return

    print("Пароль не найден.")


if __name__ == "__main__":
    # Установите целевой пароль здесь (например, 'abc123')
    target_password = input("Введите целевой пароль: ")
    n = int(input("сколько символов максимально? "))

    start_time = time.time()
    characters =  string.digits + string.ascii_letters + string.punctuation
    brute_force_password(target_password,n,characters)
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд.")
    print(string.ascii_letters)
    print(string.digits)
    print(string.punctuation)








import itertools
import string
import time


def brute_force_password(target_password,n,characters):
    # Определяем символы, которые будем использовать

    # Начинаем с длины 1 до 6 символов
    for length in range(1, n + 1):
        for guess in itertools.product(characters, repeat = length):
            guess_password = ''.join(guess)
            print(f"Пробуем: {guess_password}")

            if guess_password == target_password:
                print(f"Пароль найден: {guess_password}")
                return

    print("Пароль не найден.")


if __name__ == "__main__":
    # Установите целевой пароль здесь (например, 'abc123')
    target_password = input("Введите целевой пароль: ")
    n = int(input("сколько символов максимально? "))

    a = input("Какой набор символов(a,d,p)? ")
    characters = ""

    if "a" in a:
        characters += string.ascii_lowercase

    if "d" in a:
        characters += string.digits
    
    if "p" in a:
        characters += string.punctuation

    start_time = time.time()
    #characters =  string.digits + string.ascii_letters + string.punctuation
    brute_force_password(target_password,n,characters)
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд.")
    print(string.ascii_letters)
    print(string.digits)
    print(string.punctuation)