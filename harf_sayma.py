def harflerden_kac_adet(cumle):
    liste=[]
    for i in cumle:
        if i not in liste:
            liste.append(i)

    for i in liste:
        print i,"cümlede",cumle.count(i),"adet var"
        
