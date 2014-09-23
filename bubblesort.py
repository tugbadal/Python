def bubblesort(liste):
    for i in range(len(liste)):
        if liste[i]<liste[i+1]:
            liste[i],liste[i+1]=liste[i+1],liste[i]
    return liste
