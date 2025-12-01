def normalize_isbn(s):
    if not s:
        return ""

    s = s.replace(" ", "").replace("-", "")

    for i in s:
        if not (i.isdigit() or i == "X"):
            return ""

    if "X" in s[:-1]:
        return ""

    return s


def is_valid_isbn10(s):
    s = normalize_isbn(s)
    if len(s) != 10:
        return False

    total = 0
    for i, j in enumerate(s):
        if j == "X":
            value = 10
        else:
            value = int(j)
        peso = 10 - i
        total += peso * value

    return total % 11 == 0


def is_valid_isbn13(s):
    s = normalize_isbn(s)
    if len(s) != 13 or not s.isdigit():
        return False

    total = 0
    for i, ch in enumerate(s):
        num = int(ch)
        if i % 2 == 0:
            total += num * 1
        else:
            total += num * 3

    return total % 10 == 0


def detect_isbn(s):
    s = normalize_isbn(s)
    if len(s) == 10 and is_valid_isbn10(s):
        return "ISBN-10"
    elif len(s) == 13 and is_valid_isbn13(s):
        return "ISBN-13"
    else:
        return "INVALIDO"
    



s = input("ISBN: ")
limp=normalize_isbn(s)


if is_valid_isbn10(s):
    print("ISBN-10 válido")
    print("ISBN normalizado:", limp)
elif is_valid_isbn13(s):
    print("ISBN-13 válido")
    print("ISBN normalizado:", limp)
else:
    print("ISBN inválido")





