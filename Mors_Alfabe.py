MorsKod={'A':'.-',
        'B':'-...',
        'C':'-.-.',
        'D':'-..',
        'E':'.',
        'F':'..-.',
        'G':'--.',
        'H':'....',
        'I':'..',
        'J':'.---',
        'K':'-.-',
        'L':'.-..',
        'M':'--',
        'N':'-.',
        'O':'---',
        'P':'.--.',
        'Q':'--.-',
        'R':'.-.',
        'S':'...',
        'T':'-',
        'U':'..-',
        'V':'...-',
        'W':'.--',
        'X':'-..-',
        'Y':'-.--',
        'Z':'--..',
        'Ö':'---.',
        'Ü':'..--',
        'Ç':'-----',
        'Ş':'...-.',
        ' ':'/',
#Rakamlar
        '0':'-----',
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
#İşaretler
        '.':'.-.-.-', #nokta
        ',':'--..--', #virgül
        '?':'..--..', #soru işareti
        '-':'-....-', #tire
        '/':'-..-.',  #taksim
}

Cümle=input("Lütfen Cümleyi Giriniz:")

for i in range(0,len(Cümle)):
    indeks=Cümle[i]
    Sonuc=MorsKod.get(indeks)
    print(Sonuc,end=" ")