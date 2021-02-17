import string
import random


def main():
    phone_finished = correct_phone()
    email_finished = correct_email()
    password_finished = correct_password()
    checking(phone_finished, email_finished, password_finished)


def correct_email():
    email = input('Введите email')
    [login, domain] = email.split('@')
    if email.count('@') > 1 or email.count('@') == 0:
        print('Неверное количество знаков @')
        correct_email()
    if len(login) < 6:
        print('Логин должен содержать 6 и больше символов')
        correct_email()
    return email


def correct_phone():
    phone = input('Введите номер телефона')
    digits = ''
    for char in phone:
        if char.isdigit():
            digits += char

    if len(digits) >= 9:
        n_phone = '380' + digits[-9:]
    else:
        print('Неправильный формат')
        correct_phone()
    return n_phone


def correct_password():
    password = input('Введите пароль')
    if len(password) < 8:
        print('Пароль должен содержать минимум 8 символов')
        correct_password()
    counter_d = counter_u = counter_l = counter_s = 0
    for char in password:
        if char.isdigit():
            counter_d += 1
        elif char.isupper():
            counter_u += 1
        elif char.islower():
            counter_l += 1
        else:
            counter_s += 1

    if (counter_d and counter_u and counter_l) == 0:
        print('Пароль должен содержать минимум 1 букву в верхнем регистре, 1 в нижнем и 1 цифру')
        correct_password()
    new_password = input('Повторите пароль')
    if new_password != password:
        print('Пароли не совпадают')
        correct_password()
    return password


def checking(phone_finished, email_finished, password_finished):
    count_password = len(password_finished)
    count_password = count_password * "*"
    print(
        f"Поздравляем с успешной регистрацией!\n\
        Ваш номер телефона: {phone_finished}\n\
        Ваш email: {email_finished}\n\
        Ваш пароль: {count_password}"
    )


if __name__ == "__main__":
    main()
