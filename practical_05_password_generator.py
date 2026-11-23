import secrets


def generate_password(filename="dictionary.txt", word_count=3):
    with open(filename, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]

    if len(words) < word_count:
        raise ValueError("The dictionary must contain enough distinct words.")

    selected = secrets.SystemRandom().sample(words, word_count)
    return "-".join(selected)


if __name__ == "__main__":
    print("Generated password:", generate_password())


Sample dictionary.txt file:
apple
mango
tiger
river
school
flower
computer
orange

Generated Password: mango-tiger-school
