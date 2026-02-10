# SHA-1 Password Cracker

This project is a Python-based password cracker that attempts to reverse SHA-1 hashes
by comparing them against a list of commonly used passwords. It also supports cracking
salted hashes by prepending and appending known salts.

This project was built as part of the freeCodeCamp Information Security curriculum.

---

## How It Works

- Reads passwords from `top-10000-passwords.txt`
- Optionally reads salts from `known-salts.txt`
- Hashes each candidate using SHA-1
- Compares the result to a target hash
- Returns the matching plaintext password or a fallback message if not found

---

## Usage

```bash
python main.py

