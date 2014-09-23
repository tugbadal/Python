def remove(parca,string):
    nokta=string.index(parca)
    boy=len(parca)
    
    for i in string:
        if parca in string:
             string=string[:nokta]+string[nokta+boy:]

    print string

def sadece_birini_sil(parca,string):
    nokta=string.index(parca)
    boy=len(parca)
    if parca in string:
        string=string[:nokta]+string[(nokta+boy):]
    print string
    
 

