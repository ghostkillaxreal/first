import random
import string
import argparse

def generate_password(length=12, no_special=False, exclude_ambiguous=False):
    """Генерирует случайный пароль"""
    characters = string.ascii_letters + string.digits
    ambiguous = "lI1O0"
    
    if not no_special:
        characters += "!@#$%^&*()_+-="
    
    if exclude_ambiguous:
        characters = ''.join(c for c in characters if c not in ambiguous)
    
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=12, help="Длина пароля")
    parser.add_argument("-n", "--no-special", action="store_true", help="Без спецсимволов")
    parser.add_argument("-a", "--exclude-ambiguous", action="store_true", help="Исключить неоднозначные символы")
    args = parser.parse_args()
    
    password = generate_password(args.length, args.no_special, args.exclude_ambiguous)
    print(f"Пароль: {password}")
