import random

def veletlen():
    print("A lista elemei:")
    szamok=[]
    for i in range(50):
        szam:int=random.randint(1,100)
        szamok.append(szam)
        if i < 49:
            print(szam,end=";")
        else:
            print(szam
                  , end=" ")
    return szamok

def hettelOszthato(szamok):
    db:int=0
    for i in range(0,len(szamok),1):
        if szamok[i] % 7 == 0:
            db += 1
    return db









