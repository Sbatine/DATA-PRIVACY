# Python Cybersecurity & Data Privacy Practicals

A beginner-friendly collection of 10 Python practicals covering classical ciphers, password security, digital signatures, data privacy audits, compliance, and ethics.

## Requirements

- Python 3.8 or newer
- Internet connection only for Practical 4
- `cryptography` package only for Practical 7

Install the optional dependency:

```bash
python -m pip install -r requirements.txt
```

## Project structure

```text
python_cybersecurity_practicals/
├── practical_01_caesar_cipher.py
├── practical_02_rail_fence_cipher.py
├── practical_03_sha256_hash.py
├── practical_04_breach_check.py
├── practical_05_password_generator.py
├── practical_06_bruteforce_demo.py
├── practical_07_digital_signature.py
├── practical_08_privacy_audit.py
├── practical_09_compliance_check.py
├── practical_10_data_ethics.py
├── passwords.example.txt
├── dictionary.txt
├── requirements.txt
└── .gitignore
```

## Run a practical

From this folder, run for example:

```bash
python practical_01_caesar_cipher.py
```

Replace the filename with the practical you want to run.

## Practicals

1. Caesar cipher — encryption and decryption.
2. Rail Fence cipher — encryption and decryption.
3. SHA-256 — hash a password string.
4. Have I Been Pwned — check a password using the k-anonymity range API.
5. Password generator — combine random words from a dictionary file.
6. Brute-force demonstration — a small, offline demonstration limited to lowercase strings of up to four characters.
7. Digital signature — sign and verify a sample document with RSA-PSS.
8. Data privacy audit — a simple checklist and score.
9. Data protection compliance — a basic requirements checklist.
10. Data ethics — a simple ethical-practices checklist.

## Important security notes

- These are educational examples, not production-ready security systems.
- Do not commit real passwords, private keys, personal data, or confidential files to GitHub.
- Practical 4 uses the Have I Been Pwned Passwords range API. It sends only the first five characters of a SHA-1 hash, not the password itself or the full hash. Use only passwords you are authorized to check.
- Practical 3 demonstrates SHA-256 hashing. Plain SHA-256 is not suitable for storing real user passwords. Real applications should use a password-hashing scheme such as Argon2id, scrypt, or bcrypt.
- Practical 6 runs locally and only searches a tiny, fixed character space. Do not use it against real accounts or systems.
- Practical 7 creates a temporary key pair in memory for demonstration. A real signing workflow must securely store and manage keys.

## Example input files

- `dictionary.txt` is a small sample word list for Practical 5.
- `passwords.example.txt` shows the expected CSV-like format for Practical 4. Make a private local copy named `passwords.txt` if you want to test it. Do not upload real credentials.

## License

For educational use. You may adapt the examples for coursework.
