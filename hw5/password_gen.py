import string
import random


def generate_password_easy():
    chars = string.ascii_lowercase
    size = 8
    password = ''
    for x in range(size):
        password += random.choice(chars)
    return password


def generate_password_medium():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    size = 8
    password = ''
    for x in range(size):
        password += random.choice(chars)
    return password


def generate_password():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    size = random.randint(8, 16)
    password = ''
    for x in range(size):
        password += random.choice(chars)
    return password


while True:
    menu = input(
        "1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)\n"
        "2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)\n"
        "3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)\n"
        "4. Выход \n"
        "Сделайте выбор и нажмите Enter: "
    )
    if menu == "1":
        print(generate_password_easy())
    elif menu == "2":
        print(generate_password_medium())
    elif menu == "3":
        print(generate_password())
    elif menu == "4":
        break
    else:
        print("Повторите выбор!")
