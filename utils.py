def get_square(num):
    """Повертає квадрат числа."""
    return num * num

def is_prime(num):
    """Перевіряє, чи є число простим (ділиться тільки на 1 і на себе)."""
    if num < 2:
        return False 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_greeting(name):
    """Повертає привітання."""
    if not name:
        return "Привіт, Анонім!"
    return f"Привіт, {name}!"
