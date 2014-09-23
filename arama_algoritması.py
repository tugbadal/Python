def dogrusalArama(liste, eleman):
     liste.sort()
     for i in liste:
          if i==eleman:
               return True
          else:
               if i>eleman:
                    return False
     return False
