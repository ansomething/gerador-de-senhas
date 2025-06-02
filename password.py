from secrets import choice
from string import ascii_letters, digits


def password_generator():
    letters = ascii_letters
    numbers = digits
    symbols = "!@$%&.?_-'\""

    chars = letters + numbers + symbols
    password = "".join(choice(chars) for i in range(12))

    return password


if __name__ == "__main__":
    generated_password = password_generator()
    print(generated_password)
