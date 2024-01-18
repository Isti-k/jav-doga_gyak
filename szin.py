
def szinkeverés():
    szin:str=str(input("Kérek egy színkeverési módszert:"))
    kod:str=str(input("Kérek egy színkeverési módszert:"))
    if szin == "RGB":
        if len(kod) >= 5 and len(kod) <=11:
            print("Megfelelő hossz.")
        else:
            print("Nem megfelelő hossz.")
    if szin == "HSL":
        if len(kod) >= 7 and len(kod) <=13:
             print("Megfelelő hossz.")
        else:
            print("Nem megfelelő hossz.")
    if szin == "HEX":
        if len(kod) >= 6:
             print("Megfelelő hossz.")
        else:
            print("Nem megfelelő hossz.")
    if szin == "RGBA" or szin =="HSLA":
        print("Bonyolult kiszámolni.")






