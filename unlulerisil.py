def unlulerisil(string):
    unluler="aeiouAE�OU"
    liste=[]
    sondizi=""

    for i in string:
        liste.append(i)

    for i in string:
        if i in unluler:
            liste.remove(i)

    for i in liste:
        sondizi+=i

    print sondizi
