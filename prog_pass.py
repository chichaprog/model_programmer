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

    a = input("Какой набор символов(a,A,d,p)? ")
    characters = ""

    if "a" in a:
        characters += string.ascii_lowercase

    if "d" in a:
        characters += string.digits
    
    if "p" in a:
        characters += string.punctuation
    
    if "A" in a:
        characters += string.ascii_uppercase

    start_time = time.time()
    #characters =  string.digits + string.ascii_letters + string.punctuation
    brute_force_password(target_password,n,characters)
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд.")
    print(string.ascii_letters)
    print(string.digits)
    print(string.punctuation)