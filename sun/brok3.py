def atbash(mesaj):
    result = ""
    for char in mesaj:
        if char.isalpha():
            char = char.upper()
            ascii_val = ord(char)
            if ascii_val >= 65 and ascii_val <= 90:
                char = chr(155 - ascii_val)
            elif ascii_val >= 97 and ascii_val <= 122:
                char = chr(219 - ascii_val)
            char = char.lower()
        result += char
    return result


mesaj = ""
sifrelenmis = atbash(mesaj)
print(sifrelenmis)

def sifrele(metin, key):
    sifrelenmis = ""
    for harf in metin:
        if harf.isalpha():
            if harf.isupper():
                sifrelenmis += chr((ord(harf) + key - 65) % 26 + 65)
            else:
                sifrelenmis += chr((ord(harf) + key - 97) % 26 + 97)
        else:
            sifrelenmis += harf
    return sifrelenmis


def sifrecoz(metin, key):
    cozulmus = ""
    for harf in metin:
        if harf.isalpha():
            if harf.isupper():
                cozulmus += chr((ord(harf) - key - 65) % 26 + 65)
            else:
                cozulmus += chr((ord(harf) - key - 97) % 26 + 97)
        else:
            cozulmus += harf
    return cozulmus


def vernam(mesaj: str, anahtar: str) -> str:
    if len(anahtar) != len(mesaj):
        return "Mesaj ile Anahtar uzunluğu aynı olmalı"
    sifrelenmismesaj = ""
    for i in range(len(anahtar)):
        sifrelenmismesaj += chr(ord(mesaj[i]) ^ ord(anahtar[i]))
    return sifrelenmismesaj


mesaj = input("Mesaj Giriniz: ")
vanahtar = input("Mesaj İle aynı uzulukta bir anahtar giriniz: ")
sifrelenmis = vernam(mesaj, vanahtar)
print(sifrelenmis)

cozulmus = vernam(sifrelenmis, vanahtar)
print(cozulmus)


deger = input("şifrelenecek veri giriniz: ")
sifreli = sifrele(deger, 3)
cozulmus = sifrecoz(sifreli, 3)
print("orjinal= ", deger+"\n")
print("Şifreli= ", sifreli+"\n")
print("Çözülmüş= "+cozulmus+"\n")