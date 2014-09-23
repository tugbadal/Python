def ikilarama(liste,eleman):
    liste.sort()
    if len(liste)==0:
        return False
    else:
        orta_nokta=len(liste)/2
        if liste[orta_nokta]==eleman:
            return True
        else:
            if eleman<liste[orta_nokta]:
                return ikilarama(liste[:orta_nokta],eleman)
            else:
                return ikilarama(liste[orta_nokta+1 :],eleman)
