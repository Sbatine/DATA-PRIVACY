import hashlib


def hash_password(password):
    """Return the SHA-256 digest as a hexadecimal string."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    password = input("Enter password: ")
    print("SHA-256 Hash:", hash_password(password))

OUTPUT
Enter password: hello123

Original Password: hello123

SHA-256 Hash:
27d6b1b9b1c1a3...
