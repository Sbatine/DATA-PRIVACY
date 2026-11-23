import hashlib


def hash_password(password):
    """Return the SHA-256 digest as a hexadecimal string."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    password = input("Enter password: ")
    print("SHA-256 Hash:", hash_password(password))
