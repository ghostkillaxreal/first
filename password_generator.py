import random
import string

def generate_password(length=12):
    """Генерирует случайный пароль заданной длины"""
    # Составляющие пароля: буквы (верхний и нижний регистр), цифры, спецсимволы
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    
    # Генерация пароля
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    # Генерация пароля длиной 16 символов
    password = generate_password(16)
    print(f"Сгенерированный пароль: {password}")