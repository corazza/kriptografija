from curses.ascii import isupper


Z = 26


def to_z(c: str) -> int:
    if isupper(c):
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a')


def from_z(c: int) -> str:
    return chr(c + ord('A'))


def gen_e(plaintext: str, char_f) -> str:
    in_z = map(to_z, plaintext)
    ciphertext = map(char_f, in_z)
    in_latin = map(from_z, ciphertext)
    return ''.join(in_latin)


def gen_d(ciphertext: str, char_f) -> str:
    in_z = map(to_z, ciphertext)
    plaintext = map(char_f, in_z)
    in_latin = map(from_z, plaintext)
    return ''.join(in_latin)
