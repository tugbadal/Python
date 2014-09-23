def dizi_array_pading(matris):
    a,b=[],[]
    yeni=[]
    dahayeni=[]
    sonhali=[]
    for i in matris:
        yeni.append([i[0]]+i)
    for i in yeni:
        dahayeni.append(i+[i[len(i)-1]])

    sonhali=dahayeni
    for i in dahayeni[0]:
        a.append(i)
    for i in dahayeni[len(dahayeni)-1]:
        b.append(i)
    sonhali.insert(0,a)
    sonhali.insert(len(matris),b)
    print sonhali
    
   


                    

#aðda veri güvenliði için kullanýlýyo
