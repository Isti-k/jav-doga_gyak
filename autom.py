from Kocsi import Kocsi

def Auto():
    fajl=open("auto.txt","r",encoding="UTF-8")
    fajl.readline()
    fajl_sorok=fajl.readlines()
    fajl.close()

    kocsi_lista=[]
    for i in range(0,len(fajl_sorok),1):
        elem=fajl_sorok[i]
        lista=elem.strip().split(":")
        print(lista)
        kor:str=str(lista[0])
        kiir:int=int(lista[1])
        kocsi=Kocsi(kor,kiir)
        kocsi_lista.append(kocsi)

    return kocsi_lista

def flotta():
    """"""



