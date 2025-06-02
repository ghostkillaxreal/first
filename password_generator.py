import random
import string
import argparse

def generate_password(length=12, no_special=False, exclude_ambiguous=False):
    characters = string.ascii_letters + string.digits
    ambiguous = "lI1O0"
    
    if not no_special:
        characters += "!@#$%^&*()_+-="
    
    if exclude_ambiguous:
        # Исправление: убираем неоднозначные символы из всех категорий
        characters = ''.join(c for c in characters if c not in ambiguous)
    
    return ''.join(random.choice(characters) for _ in range(length))

# ... (остальной код без изменений)
