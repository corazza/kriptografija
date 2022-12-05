import IPython
import itertools
import sys

import cezar
import afina
import cezarova_kljucna
from util import *


def prvi_zadatak():
    """
    6 => DOZVOLA
    """
    print('=== PRVI ZADATAK ===')
    cezar.break_cipher('JUFBURG')


def drugi_zadatak():
    """
    (11, 2) => CHARL ESBAB BAGEJ EJEDA NODPR VIHKR IPTOL OGAKO JIJEU KRIPT OLOGI JUUNI OIUPO TREBL JAVAO MATEM ATICK EPOST UPKEI FORMU LERAZ BIJAO JEPOL IALFA BETSK ESIFR EUVRI JEMEK ADSEJ OSVJE ROVAL ODAIH JENEM OGUCE DEKRI PTIRA TI
    """
    print('=== DRUGI ZADATAK ===')
    cipher = """YBCHT USNCN NCQUX UXUJC PAJLH ZMBIH MLDAT AQCIA
XMXUO IHMLD ATAQM XOOPM AMOLA DHUNT XCZCA ECDUE
CDMYI ULASD OLIUM FAHEO TUHCR NMXCA XULAT MCTFC
NUDSI USMFH UOZHM XUEUI CJSUX ASZXU HAZCT AJCMB
XUPUE AQOYU JUIHM LDMHC DM"""

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
                if len(set(['Q', 'X', 'W', 'Y']).intersection(set(d))) == 0:
                    print(f'{key} => {d}')
            except:
                pass


def treci_zadatak():
    """
    (vukovar, 7) => VELIK IFRAN CUSKI MATEM ATICA RFRAN COISV IETES
MATRA SEOSN IVACE MMODE RNEAL GEBRE BIOJE TAKOD
JERIP OZNAT IKRIP TOANA LITIC ARKOJ ISEOS OBITO
ISTAK AODEK RIPTI RANJE MSIFR IRANI HSPAN JOLSK
IHPOR UKA
    """
    print('=== TRECI ZADATAK ===')
    cipher = """JXAUO UYFQB TIGOU RQHXR QHUTQ FYFQB TCUGJ UXHXG
RQHFQ GXCGB UJQTX RRCWX FBXQA ZXSFX SUCKX HQOCW
KXFUD CPBQH UOFUD HCQBQ AUHUT QFOCK UGXCG CSUHC
UGHQO QCWXO FUDHU FQBKX RGUYF UFQBU VGDQB KCAGO
UVDCF IOQ"""

    cipher2 = """WKZTS KZQYU MAZAU ZPZVD TQMAO ZUENK EAUVD FVDAQ
ZAFVD ZRNVA CENUV RLMKD TAMFM ODTNV BZMBW MPTCA
UZYAZ WMKMK ZDTAZ VDTNK VPBTR UVDZD TUKZN CVMOM
BZCZQ MKTRE QZVFZ ATVSC KZACV XVSZO M"""

    gradovi = ['vukovar', 'dubrovnik']  # hint

    for grad in gradovi:
        for i in range(Z):
            p = cezarova_kljucna.get_permutation(grad, i)
            plaintext = cezarova_kljucna.apply_permutation(cipher2, p)
            if 'JE' in plaintext.replace(' ', ''):
                print(f'({grad}, {i}) => {plaintext}')


def main():
    prvi_zadatak()
    drugi_zadatak()
    treci_zadatak()


if __name__ == '__main__':
    main()
