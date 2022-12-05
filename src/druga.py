import IPython
import math

from util import *


def matrica(m: int, cipher: list[int]) -> list[list[int]]:
    n = len(cipher)
    num_rows = m
    num_columns = math.ceil(n/num_rows)
    result = [[-1 for i in range(num_columns)] for j in range(num_rows)]
    for k in range(n):
        i = k % num_rows
        j = k // num_rows
        result[i][j] = cipher[k]
    return result


def frequencies(cipher: list[int]) -> dict[int, int]:
    counter = {c: 0 for c in range(Z)}
    for c in cipher:
        if c != -1:
            counter[c] += 1
    return counter


def IC(cipher: list[int]) -> float:
    """Indeks koincidencije"""
    n = len(cipher)
    counter = frequencies(cipher)
    r = 0
    for i in range(Z):
        r += float(counter[i] * (counter[i] - 1)) / float(n * (n - 1))
    return r


def M(cipher: list[int], g) -> float:
    n = len(cipher)
    counter = frequencies(cipher)
    r = 0
    for i in range(Z):
        r += float(PROMILI[from_z(i)] / 1000.0) * \
            counter[(Z + i - g) % Z] / float(n)
    return r


def duljina_kljuca(cipher: list[int]) -> int:
    best = None
    for m in range(2, 10):
        mat = matrica(m, cipher)
        ics = [IC(redak) for redak in mat]
        mse = sum([(ic - 0.064)**2 for ic in ics]) / len(ics)
        if best == None:
            best = (m, mse)
        else:
            if mse < best[1]:
                best = (m, mse)
    return best[0]


def d(cipher: list[int], kljuc: list[int]) -> list[int]:
    m = len(kljuc)
    r = []
    for i in range(len(cipher)):
        k = kljuc[i % m]
        # k = kljuc[i] if i < m else cipher[i - m]
        r.append((cipher[i] - k) % Z)
    return r


def prvi():
    """
    5
    SPLIT
    LEONBATTISTAALBERTISMATRASEOCEMZAPADNEKRIPTOLOGIJEIZUMIOJEPRVUPOLIALFABETSKUSIFRUISIFRIRANIKODVELIKEDRZAVESUPOCELESIFRIRATISVOJEKODNERIJECITEKCETIRISTOGODINAKASNIJE
    """
    cipher = """DTZVU SIEQL LPLTU WGEQL EPEZT KTZKX EOLXT VCPSKAEEWE GVTRX AOFUB GYPXK NJAWE APWNT TTEAD MHTNKMXDQY JXCIG AZZLO WATSX VGKIO WHFXH UTWML AUCQKSITAO GYPSH VCPZB BTNQM WZNMM AGTAM GVZLB FPVIL FXUM"""
    cipher_z = str_to_z(cipher)
    m = duljina_kljuca(cipher_z)
    mat = matrica(m, cipher_z)
    kljuc = []
    for j in range(m):
        mgs = [(g, M(mat[j], g)) for g in range(0, Z)]
        mgs = sorted(mgs, key=lambda tup: -tup[1])
        mg = mgs[0][0]
        kljuc.append((Z - mg) % Z)
    print(m)
    print(z_to_str(kljuc))
    print(z_to_str(d(cipher_z, kljuc)))


def drugi():
    """PO GY MD ZK HO OH EM"""
    pass


def treci():
    """kvadrat(5, 9, 11, 15)"""
    print(str_to_z('VERNAM'))
    print(str_to_z('TNUXCS'))


def main():
    prvi()
    drugi()
    treci()


if __name__ == "__main__":
    main()
