from curses.ascii import isalpha, isspace, isupper


Z = 26


def str_to_z(cs: str) -> list[int]:
    r = []
    for c in cs:
        if isalpha(c):
            r.append(to_z(c))
        else:
            r.append(-1)
    return _filter_whitespace(r)


def z_to_str(zs: list[int]) -> str:
    r = []
    for z in zs:
        if z != -1:
            r.append(from_z(z))
        else:
            r.append(' ')
    return ''.join(r)


def to_z(c: str) -> int:
    if isupper(c):
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a')


def from_z(c: int) -> str:
    return chr(c + ord('A'))


def applier(plaintext: str, char_f) -> str:
    in_z = str_to_z(plaintext)
    ciphertext = map(lambda z: _apply_char_f(z, char_f), in_z)
    in_latin = z_to_str(ciphertext)
    return ''.join(in_latin)


def _apply_char_f(z: int, char_f) -> int:
    if z == -1:
        return -1
    else:
        return char_f(z)


def _filter_whitespace(in_z: list[int]) -> list[int]:
    return list(filter(lambda z: z != -1, in_z))


PROMILI = {
    'A':	115,
    'I':	98,
    'O':	90,
    'E':	84,
    'N':	66,
    'S':	56,
    'R':	54,
    'J':	51,
    'T':	48,
    'U':	43,
    'D':	37,
    'K':	36,
    'V':	35,
    'L':	33,
    'M':	31,
    'P':	29,
    'C':	28,
    'Z':	23,
    'G':	16,
    'B':	15,
    'H':	8,
    'F':	3,
    'Q': 0,
    'W': 0,
    'X': 0,
    'Y': 0
}
