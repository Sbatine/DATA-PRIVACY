def encrypt(text, rails):
    if rails < 2:
        raise ValueError("Number of rails must be at least 2.")

    fence = [[] for _ in range(rails)]
    row, direction = 0, 1

    for char in text:
        fence[row].append(char)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return "".join("".join(line) for line in fence)


def decrypt(cipher, rails):
    if rails < 2:
        raise ValueError("Number of rails must be at least 2.")

    # Recreate the zigzag row pattern.
    pattern = []
    row, direction = 0, 1

    for _ in cipher:
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    # Fill each rail with its corresponding ciphertext characters.
    rail_counts = [pattern.count(r) for r in range(rails)]
    rail_chars = []
    index = 0

    for count in rail_counts:
        rail_chars.append(list(cipher[index:index + count]))
        index += count

    positions = [0] * rails
    result = []

    for rail in pattern:
        result.append(rail_chars[rail][positions[rail]])
        positions[rail] += 1

    return "".join(result)


if __name__ == "__main__":
    message = input("Enter message: ")
    rails = int(input("Enter number of rails: "))

    encrypted = encrypt(message, rails)
    decrypted = decrypt(encrypted, rails)

    print("Encrypted text:", encrypted)
    print("Decrypted text:", decrypted)

OUTPUT
Enter password: hello123

Original Password: hello123

SHA-256 Hash:
27d6b1b9b1c1a3...
