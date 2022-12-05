from typing import Tuple
from math import gcd
import IPython
import itertools

from util import *

INVERSE = {
    1: 1,
    3: 9,
    5: 21,
    7: 15,
    9: 3,
    11: 19,
    15: 7,
    17: 23,
    19: 11,
    21: 5,
    23: 17,
    25: 25
}


def _e(k: Tuple[int, int], c: int) -> int:
    assert gcd(k[0], Z) == 1
    return (k[0]*c + k[1]) % Z


def _d(k: Tuple[int, int], c: int) -> int:
    assert gcd(k[0], Z) == 1
    return (INVERSE[k[0]]*(c - k[1])) % Z


def e(k: Tuple[int, int], plaintext: str) -> str:
    return applier(plaintext, lambda c: _e(k, c))


def d(k: Tuple[int, int], ciphertext: str) -> str:
    return applier(ciphertext, lambda c: _d(k, c))


def _n_most_frequent(n: int, length: int, in_z: list[int]) -> list[int]:
    counter = {}
    for i in range(len(in_z) - length + 1):
        z = tuple(in_z[i:i+length])
        if z not in counter:
            counter[z] = 0
        counter[z] += 1
    grouped = {}
    for key, val in counter.items():
        if val not in grouped:
            grouped[val] = []
        grouped[val].append(key)

    counter_list = sorted(list(grouped.items()), key=lambda x: -x[0])
    return list(map(lambda x: x[1], counter_list[0:n]))


def n_most_frequent(n: int, length: int, plaintext: str) -> list[str]:
    in_z = str_to_z(plaintext)
    most_frequent = _n_most_frequent(n, length, in_z)
    return [[''.join(z_to_str(zs)) for zs in zss] for zss in most_frequent]


def solve_key(a: str, i: str) -> Tuple[int, int]:
    k_b = to_z(a)

    for k_a in INVERSE:
        if (to_z('I')*k_a + k_b) % 26 == to_z(i):
            return (k_a, k_b)

    raise ValueError()
