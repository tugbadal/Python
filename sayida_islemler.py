def basamaklar_toplami(sayi):
    toplam=0
    sayi=str(sayi)
    for i in sayi:
        toplam+=int(i)
    return toplam

def tekler_toplami(sayi):
    toplam=0
    sayi=str(sayi)
    for i in sayi:
        if (int(i)%2)==1:
            toplam+=int(i)
    return toplam

def enbuyuk_basamak(sayi):
    sayi=str(sayi)
    enbuyuk=0
    for i in sayi:
        if int(i)>enbuyuk:
            enbuyuk=int(i)
    return enbuyuk
   
#    if enbuyuk==int(sayi[len(sayi)]):
#       print "ve",enbuyuk,"sayinin birler basamag�ndad�r"
#    elif enbuyuk==int(sayi[len(sayi)-1]):
#       print "ve",enbuyuk,"sayinin onlar basamag�ndad�r"
#    elif enbuyuk==int(sayi[len(sayi)-2]):
#       print "ve",enbuyuk,"sayinin y�zler basamag�ndad�r"
#    elif enbuyuk==int(sayi[len(sayi)-3]):
#       print"ve",enbuyuk,"sayinin binler basamag�ndad�r"
#    elif enbuyuk==int(sayi[len(sayi)-4]):
#        print "ve",enbuyuk,"sayinin onbinler baasamag�ndad�r"
    
def enbuyuk_sayiyi_olustur(sayi):
    sayi=str(sayi)
    liste=list(sayi)
    yeni=""
    while(liste!=[]):
        yeni+=max(liste)
        liste.remove(max(liste))
    print yeni

def terscevir(sayi):
    pass
    

            
    
    
            
