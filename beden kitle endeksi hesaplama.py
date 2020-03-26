print("beden kitle endeksi hesaplama programına hoşgeldiniz")


kilo= int(input("kilonuzu giriniz"))
boy= float(input("boyunuzu giriniz"))


def bki_():
    bki = kilo / (boy**2)
    if bki < 18.50:
        print("zayıf")
    elif 18.50 <= bki < 25:
        print("normal")
    elif 25 <= bki < 30:
        print("fazla kilolu")
    else:
        print ("obez")
    

bki_()
