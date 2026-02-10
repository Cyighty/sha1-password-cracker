import hashlib
import os

_DIR = os.path.dirname(os.path.abspath(__file__))
_PASSWORDS_FILE = os.path.join(_DIR, "top-10000-passwords.txt")
_SALTS_FILE = os.path.join(_DIR, "known-salts.txt")


def _sha1_hex(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def _read_lines(path: str):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s:
                yield s


def crack_sha1_hash(hash: str, use_salts: bool = False) -> str:
    target = (hash or "").strip().lower()

    if not use_salts:
        for pwd in _read_lines(_PASSWORDS_FILE):
            if _sha1_hex(pwd) == target:
                return pwd
        return "PASSWORD NOT IN DATABASE"

    salts = list(_read_lines(_SALTS_FILE))
    for pwd in _read_lines(_PASSWORDS_FILE):
        for salt in salts:
            if _sha1_hex(salt + pwd) == target:
                return pwd
            if _sha1_hex(pwd + salt) == target:
                return pwd

    return "PASSWORD NOT IN DATABASE"
