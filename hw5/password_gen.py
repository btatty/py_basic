import string
import random


def main():
    choice = input(
        "1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)\n"
        "2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)\n"
        "3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)\n"
        "Сделайте выбор и нажмите Enter: "
    )
    if choice == "1":
        print(gen_password(string.ascii_lowercase))
    elif choice == "2":
        print(gen_password(string.ascii_letters + string.digits))
    elif choice == "3":
        print(gen_strong_password())


def gen_password(chars, length=8):
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password


def gen_strong_password():
    length = random.randint(8, 16)
    password = gen_password(string.digits + string.ascii_letters + string.punctuation, length)

    counter_d = counter_u = counter_l = counter_s = 0
    for char in password:
        if char.isdigit():
            counter_d += 1
        elif char.isupper():
            counter_u += 1
        elif char.islower():
            counter_l += 1
        elif not char.isspace():
            counter_s += 1

    if counter_d and counter_u and counter_l and counter_s:
        return password
    return gen_strong_password()


if __name__ == '__main__':
    main()
