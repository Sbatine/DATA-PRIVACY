import itertools
import string


def brute_force_demo(target, max_length=4):
    """
    Educational offline demonstration only.
    Tries lowercase ASCII strings up to max_length.
    """
    characters = string.ascii_lowercase

    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            guess = "".join(combination)
            if guess == target:
                return guess

    return None


if __name__ == "__main__":
    target = input("Enter a lowercase test password (max 4 letters): ")

    if not target.isalpha() or not target.islower() or len(target) > 4:
        print("Please use 1-4 lowercase letters for this demonstration.")
    else:
        result = brute_force_demo(target)
        if result:
            print("Password found:", result)
        else:
            print("Password not found within the search limit.")


Sample Output:
Enter a test password: cat

Password found: cat
