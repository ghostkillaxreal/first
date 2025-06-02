import random
import string
import argparse

# ... (предыдущие функции)

def check_strength(password):
    """Проверяет сложность пароля"""
    strength = 0
    if any(c.islower() for c in password): strength += 1
    if any(c.isupper() for c in password): strength += 1
    if any(c.isdigit() for c in password): strength += 1
    if any(c in "!@#$%^&*()_+-=" for c in password): strength += 1
    return strength

if __name__ == "__main__":
    # ... (предыдущий код аргументов)
    
    for i in range(args.count):
        password = generate_password(args.length, args.no_special, args.exclude_ambiguous)
        strength = check_strength(password)
        print(f"Пароль {i+1} ({strength}/4): {password}")
