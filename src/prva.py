import IPython
import itertools

import cezar
import afina
from util import *


def prvi_zadatak():
    cezar.break_cipher('JUFBURG')


def drugi_zadatak():
    cipher = """YBCHT USNCN NCQUX UXUJC PAJLH ZMBIH MLDAT AQCIA
XMXUO IHMLD ATAQM XOOPM AMOLA DHUNT XCZCA ECDUE
CDMYI ULASD OLIUM FAHEO TUHCR NMXCA XULAT MCTFC
NUDSI USMFH UOZHM XUEUI CJSUX ASZXU HAZCT AJCMB
XUPUE AQOYU JUIHM LDMHC DM"""

    # cipher2 = 'OZWHRYEZCVWFCTPCUWRCFPYHWI'
    most_frequent_grouped = afina.n_most_frequent(5, 1, cipher)
    most_frequent_2gram = afina.n_most_frequent(5, 2, cipher)

    most_frequent = list(itertools.chain(*most_frequent_grouped))

    print(most_frequent_grouped)
    print(most_frequent_2gram)

    for a in most_frequent:
        for i in most_frequent:
            try:
                key = afina.solve_key(a, i)
                d = afina.d(key, cipher)
                # if len(set(['Q', 'X', 'W', 'Y']).intersection(set(d))) == 0:
                print(d, key)
            except:
                pass

    # for a in range(26):
    #     for i in range(26):
    #         try:
    #             key = afina.solve_key(from_z(a), from_z(i))
    #             d = afina.d(key, cipher)
    #             if len(set(['Q', 'X', 'W', 'Y']).intersection(set(d))) == 0:
    #                 print(d, key)
    #         except:
    #             pass


def main():
    # prvi_zadatak()
    drugi_zadatak()


if __name__ == '__main__':
    main()
