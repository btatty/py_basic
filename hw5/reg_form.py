def correct_email():
    if email.count('@') > 1 or email.count('@') == 0:
        return False, 'Неверное количество знаков @'
    [login, domain] = email.split('@')
    if len(login) < 6:
        return False, 'Логин должен содержать 6 и больше символов'
    return email


def correct_phone():
    digits = ''
    for char in phone:
        if char.isdigit():
            digits += char

    if len(digits) >= 9:
        n_phone = '380' + digits[-9:]
    else:
        return False, 'Неправильный формат'
    return n_phone


def has_digits():
    return any(char.isdigit() for char in password)


def has_uppers():
    return any(char.isupper() for char in password)


def has_lowers():
    return any(char.islower() for char in password)


def correct_password():
    if len(password) < 8:
        return False, 'Пароль должен содержать минимум 8 символов'
    if has_digits() and has_lowers() and has_uppers() == 0:
        return 'Пароль должен содержать минимум 1 букву в верхнем регистре, 1 в нижнем и 1 цифру'
    return password


def ask_password():
    if new_password == password:
        print('Вы успешно прошли регестрацию')
    else:
        print('Пароли не совпадают')
    return new_password


if __name__ == "__main__":
    phone = input('Введите номер телефона')
    print(correct_phone())
    email = input('Введите email')
    print(correct_email())
    password = input('Введите пароль')
    print(correct_password())
    new_password = input('Повторите пароль')
    print(ask_password())
