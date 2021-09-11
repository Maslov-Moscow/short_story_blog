import random
import string


def gen_password() -> str:
    """Генерация кода подтверждения"""
    length = 12

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols

    temp = random.sample(all, length)

    return "".join(temp)
