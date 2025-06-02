import random
import string
import argparse

def generate_password(length=12, no_special=False, exclude_ambiguous=False):
    # ... (предыдущая реализация функции)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=12, help="Длина пароля")
    parser.add_argument("-n", "--no-special", action="store_true", help="Без спецсимволов")
    parser.add_argument("-a", "--exclude-ambiguous", action="store_true", help="Исключить неоднозначные символы")
    parser.add_argument("-c", "--count", type=int, default=1, help="Количество паролей")
    args = parser.parse_args()
    
    for i in range(args.count):
        password = generate_password(args.length, args.no_special, args.exclude_ambiguous)
        print(f"Пароль {i+1}: {password}")
