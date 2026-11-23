import hashlib
import urllib.error
import urllib.request


def check_password(password):
    """
    Check a password with the Have I Been Pwned range API.
    Returns the breach count, 0 if not found, or None on an API error.
    """
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Python-Educational-Practical",
            "Add-Padding": "true",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            data = response.read().decode("utf-8")

        for line in data.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix.upper() == suffix:
                return int(count)

        return 0

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("API error:", error)
        return None


if __name__ == "__main__":
    print("Use only test credentials or passwords you are authorized to check.")
    print("Expected file format: username,password")

    try:
        with open("passwords.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                username, password = line.split(",", 1)
                count = check_password(password)

                if count is None:
                    print(f"{username}: Could not check password.")
                elif count > 0:
                    print(f"{username}: Password found in breaches ({count} occurrences).")
                else:
                    print(f"{username}: No match found in the breach corpus.")
    except FileNotFoundError:
        print("Create a local passwords.txt file using passwords.example.txt as a template.")



SAMPLE
user1,password123
user2,hello987

Sample Output:
user1 Password leaked!
user2 Password not found.
