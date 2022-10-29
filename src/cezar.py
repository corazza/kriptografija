from util import *


def _e(k: int, c: int) -> int:
    return (c + k) % Z


def _d(k: int, c: int) -> int:
    return (c - k) % Z


def e(k: int, plaintext: str) -> str:
    return applier(plaintext, lambda c: _e(k, c))


def d(k: int, ciphertext: str) -> str:
    return applier(ciphertext, lambda c: _d(k, c))


def break_cipher(ciphertext: str) -> str:
    for k in range(1, Z):
        print(d(k, ciphertext), k)
