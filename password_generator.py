import random
import string
import argparse

def generate_password(length=12, no_special=False):
    """Генерирует случайный пароль"""
    characters = string.ascii_letters + string.digits
    if not no_special:
        characters += "!@#$%^&*()_+-="
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=12, help="Длина пароля")
    parser.add_argument("-n", "--no-special", action="store_true", help="Без спецсимволов")
    args = parser.parse_args()
    
    password = generate_password(args.length, args.no_special)
    print(f"Пароль: {password}")
