import IPython

import cezar
import afina


def prvi_zadatak():
    cezar.break_cipher('JUFBURG')


def drugi_zadatak():
    plaintext = 'ZADAR'
    k = (7, 3)
    print(afina.e(k, plaintext))


def main():
    drugi_zadatak()


if __name__ == '__main__':
    main()
