with open("CSV/szolgaltatasok.csv", "r") as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(";")
        szolgaltat_azon_azon.append(adatok[0])
        szolgaltat_nev.append(adatok[1])
        szolgaltat_koltseg.append(adatok[2])
        szolgaltat_kezdo.append(adatok[3])
        szolgaltat_vegzo.append(adatok[4])
        szolgaltat_epazon.append(adatok[5])