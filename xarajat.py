"""Kunlik xarajatlarni yozib boradigan kichik dastur."""

XARAJATLAR = []


def qoshish(summa, izoh):
    XARAJATLAR.append({"summa": summa, "izoh": izoh})


def jami():
    return sum(x["summa"] for x in XARAJATLAR)


def eng_katta():
    """Eng qimmat xarajatni qaytaradi."""
    return max(XARAJATLAR, key=lambda x: x["summa"], default=None)


if __name__ == "__main__":
    qoshish(12000, "Non va sut")
    qoshish(45000, "Taksi")
    print(f"Jami: {jami():,} so'm")
