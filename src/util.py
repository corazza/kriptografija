from curses.ascii import isalpha, isspace, isupper


Z = 26


def to_z(c: str) -> int:
    if isupper(c):
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a')


def from_z(c: int) -> str:
    return chr(c + ord('A'))


def str_to_z(cs: str) -> list[int]:
    r = []
    for c in cs:
        if isalpha(c):
            r.append(to_z(c))
        else:
            r.append(-1)
    return r


def z_to_str(zs: list[int]) -> str:
    r = []
    for z in zs:
        if z != -1:
            r.append(from_z(z))
        else:
            r.append(' ')
    return ''.join(r)


def apply_char_f(z: int, char_f) -> int:
    if z == -1:
        return -1
    else:
        return char_f(z)


def applier(plaintext: str, char_f) -> str:
    in_z = str_to_z(plaintext)
    ciphertext = map(lambda z: apply_char_f(z, char_f), in_z)
    in_latin = z_to_str(ciphertext)
    return ''.join(in_latin)


def filter_whitespace(in_z: list[int]) -> list[int]:
    return list(filter(lambda z: z != -1, in_z))
