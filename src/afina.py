from typing import Tuple
from math import gcd

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
    return gen_e(plaintext, lambda c: _e(k, c))


def d(k: int, ciphertext: str) -> str:
    return gen_d(ciphertext, lambda c: _d(k, c))
