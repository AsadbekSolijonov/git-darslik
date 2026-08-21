"""Xarajatlar bo'yicha qisqa hisobot chiqaradi."""


def hisobot(xarajatlar):
    for x in xarajatlar:
        print(f"{x['izoh']:<20} {x['summa']:>8,}")
