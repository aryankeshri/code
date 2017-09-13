import random


def generate_code():
    chars = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        value = "".join(random.choice(chars) for _ in range(6))
        return value
