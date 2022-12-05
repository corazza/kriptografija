import IPython

from util import *


def apply_permutation(cipher: str, p: dict[str, str]) -> str:
    r = ''
    for c in cipher:
        if c in p:
            r = f'{r}{p[c]}'
        elif c != '\n':
            r = f'{r} '
        else:
            r = f'{r}{c}'
    return r


def get_permutation(keyword: str, position: int) -> dict[str, str]:
    keyword = keyword.upper()
    keys = list(map(from_z, range(Z)))
    used = set()
    p = {key: ' ' for key in keys}
    for i in range(len(keyword)):
        if keyword[i] not in used:
            position = position % Z
            p[keys[position]] = keyword[i]
            used.add(keyword[i])
            position += 1
    not_used = sorted(list(set(keys) - used))
    for i in range(len(not_used)):
        position = position % Z
        p[keys[position]] = not_used[i]
        position += 1
    return {v: k for k, v in p.items()}
