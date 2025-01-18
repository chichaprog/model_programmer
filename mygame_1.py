def main():
    print("Добро пожаловать в текстовую игру!")
    player_name = input("Введите ваше имя: ")
    print(f"Привет, {player_name}! Приготовьтесь к приключению.")

    has_key = False

    while True:
        command = input("Введите команду (идти, осмотреться, взять ключ, выйти): ").strip().lower()

        if command == "выйти":
            print("Спасибо за игру!")
            break
        elif command == "идти":
            if has_key:
                print("Вы открыли дверь и вышли на свободу! Победа!")
                break
            else:
                print("Дверь заперта. Вам нужен ключ.")
        elif command == "осмотреться":
            print("Вы видите дверь и ключ на столе.")
        elif command == "взять ключ":
            has_key = True
            print("Вы взяли ключ.")
        else:
            print("Неизвестная команда.")

# if __name__ == "main":
main()