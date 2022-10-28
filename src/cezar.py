from curses.ascii import isupper


Z = 26


def to_z(c: str) -> int:
    if isupper(c):
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a')


def from_z(c: int) -> str:
    return chr(c + ord('A'))


def _e(k: int, c: int) -> int:
    return (c + k) % Z


def _d(k: int, c: int) -> int:
    return (c - k) % Z


def e(k: int, plaintext: str) -> str:
    in_z = map(to_z, plaintext)
    ciphertext = map(lambda c: _e(k, c), in_z)
    in_latin = map(from_z, ciphertext)
    return ''.join(in_latin)


def d(k: int, ciphertext: str) -> str:
    in_z = map(to_z, ciphertext)
    plaintext = map(lambda c: _d(k, c), in_z)
    in_latin = map(from_z, plaintext)
    return ''.join(in_latin)


def break_cipher(ciphertext: str) -> str:
    for k in range(1, Z):
        print(d(k, ciphertext), k)
