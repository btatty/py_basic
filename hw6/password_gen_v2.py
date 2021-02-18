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
        password = gen_password(string.ascii_lowercase)
    elif choice == "2":
        password = gen_password(string.ascii_letters + string.digits)
    elif choice == "3":
        password = gen_strong_password()
    print("password: ", password)
    check_password(password)


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


def save_password(password):
    with open("data.txt", "a") as f:
        f.write(f"{password}\n")
    return main()


def check_password(password):
    with open("data.txt", "r") as f:
        read = f.read()
        read = read.split("\n")
        a = 0
        for i in read:
            if i == password:
                a = 1
    if a == 1:
        print(f"The password is repeated:{password}\nTry again")
        return main()
    else:
        return save_password(password)


if __name__ == '__main__':
    main()
