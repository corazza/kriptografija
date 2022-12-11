def flip(x: int) -> int:
    return -x


def dodaj_c(x: int) -> int:
    return x+3


def dodaj_malog(x: int) -> int:
    return 2*x


# x = medvjed
# y = carapa
for x in range(100):
    prva = dodaj_malog(x) + x + x
    if prva != 36:
        continue
    for y in range(100):
        treca = y + dodaj_malog(y) + y
        if treca != 24:
            continue
        print(flip(dodaj_malog(x)) / flip(dodaj_c(y)) + 3)
        print(x, 3, y)
