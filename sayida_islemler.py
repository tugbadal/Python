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
#       print "ve",enbuyuk,"sayinin birler basamagındadır"
#    elif enbuyuk==int(sayi[len(sayi)-1]):
#       print "ve",enbuyuk,"sayinin onlar basamagındadır"
#    elif enbuyuk==int(sayi[len(sayi)-2]):
#       print "ve",enbuyuk,"sayinin yüzler basamagındadır"
#    elif enbuyuk==int(sayi[len(sayi)-3]):
#       print"ve",enbuyuk,"sayinin binler basamagındadır"
#    elif enbuyuk==int(sayi[len(sayi)-4]):
#        print "ve",enbuyuk,"sayinin onbinler baasamagındadır"
    
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
    

            
    
    
            
