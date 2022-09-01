# Hesap Makinesi :)

def toplama(sayı1, sayı2):
    return sayı1 + sayı2

def cıkarma(sayı1, sayı2):
    return sayı1 - sayı2

def carpma(sayı1, sayı2):
    return sayı1 * sayı2

def bolme(sayı1, sayı2):
    return sayı1 / sayı2

# Hesap Makinesine Giriş

print("İşlemlerinizi giriniz \n",
        "1. toplama \n"
        "2. cıkarma \n"
        "3. carpma \n"
        "4. bolme" 

)

ıslem=int(input("işlem 1,2,3,4" \
    "olsun:"))   

sayı1=int(input("bırıncı sayı:"))
sayı2=int(input("ıkıncı sayı:"))

if ıslem ==1:
    print(sayı1, "+", sayı2, "=", toplama(sayı1, sayı2))

if ıslem ==2:
    print(sayı1, "-", sayı2, "=", cıkarma(sayı1, sayı2))

if ıslem ==3:
    print(sayı1, "*", sayı2, "=", carpma(sayı1, sayı2))

if ıslem ==4:
    print(sayı1, "/", sayı2, "=", bolme(sayı1, sayı2))