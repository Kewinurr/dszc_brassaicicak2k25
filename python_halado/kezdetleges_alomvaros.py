import random
import csv
import datetime
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

epulet_azon = []
epulet_nev = []
epulet_tipus = []
epulet_ev = []
epulet_hasznos = []
epulet_allapot = []


with open('CSV/epuletek.csv', 'r') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        epulet_azon.append(int(adatok[0]))
        epulet_nev.append(adatok[1].strip('"'))
        epulet_tipus.append(adatok[2].strip('"'))
        epulet_ev.append(int(adatok[3]))
        epulet_hasznos.append(int(adatok[4].strip('"')))
        epulet_allapot.append(int(random.randint(1,5)))


lakos_azon = []
lakos_nev = []
lakos_szul = []
lakos_foglal = []
lakos_lakohely = []
with open("CSV/lakosok.csv", "r") as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(";")
        lakos_azon.append(int(adatok[0]))
        lakos_nev.append(adatok[1].strip('"'))
        lakos_szul.append(int(adatok[2]))
        lakos_foglal.append(adatok[3].strip('"'))
        lakos_lakohely.append(int(adatok[4]))



projekt_azon = []
projekt_nev = []
projekt_koltseg = []
projekt_kezdo_alap = []
projekt_vegzo_alap = []
projekt_kezdo = []
projekt_vegzo = []
projekt_epazon = []
with open("CSV/projektek.csv", "r") as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(";")
        projekt_azon.append(int(adatok[0]))
        projekt_nev.append(adatok[1].strip('"'))
        projekt_koltseg.append(int(adatok[2]    ))
        projekt_kezdo.append(adatok[3].strip('"'))  
        projekt_vegzo.append(adatok[4].strip('"'))
        projekt_epazon.append(adatok[5].strip('"'))
from datetime import datetime


for datum_str in projekt_kezdo_alap:
    try:
        datum = datetime.strptime(datum_str, "%Y.%m.%d").date()
        projekt_kezdo.append(datum)
    except ValueError:
        print(f"Hibás dátum: {datum_str}")

print(date_objects)
# Hibás dátum: 2025.13.01
# [date(2025, 1, 1), date(2023, 12, 31), date(2024, 6, 15)]

szolgaltat_azon = []
szolgaltat_nev = []
szolgaltat_tipus = []
szolgaltat_epazon = []
with open("CSV/szolgaltatasok.csv", "r") as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(";")
        szolgaltat_azon.append(adatok[0].strip('"'))
        szolgaltat_nev.append(adatok[1].strip('"'))
        szolgaltat_tipus.append(adatok[2].strip('"'))
        szolgaltat_epazon.append(adatok[3].strip('"'))


while True:
    elegedettseg = int(input("Város lakosainak elégedettsége (2-100 között): "))
    if elegedettseg in range(2, 101):
        break
min_elegedettseg = 0
while min_elegedettseg == 0:
    if elegedettseg < 15:
        min_elegedettseg = random.randint(1,elegedettseg-1)
    elif elegedettseg > 15 and elegedettseg < 25:
        min_elegedettseg = random.randint(1,10)
    else:
        min_elegedettseg = random.randint(1,elegedettseg-15)
print(min_elegedettseg)
penzkeret = int(input("MAX pénz összeg a városban zajló fejlesztésekre: "))


#Épületek adatainak kiegészítése egy jelzővel (pl. jó, vagy 1-5-ös skálán) [STRING/INT], ha már megvan a CSV fájlunk.
#Szolgáltatások havi költsége, ha már megvan a CSV fájlunk

lehetseges_fejl = ["Új épület építése", "Karbantartás meglévő épületen", "Új szolgáltatás bevezetése", "Szolgáltatás megszüntetése"]
while True:
    fejlesztes_szama = int(input("\nFejlesztési döntések (A fejlesztése döntések számának a beírásával választod ki.)\n\t1. Új épület építése\n\t2. Karbantartás meglévő épületen\n\t3. Új szolgáltatás bevezetése\n\t4. Szolgáltatás megszüntetése\nVálassz egyet: "))
    if fejlesztes_szama in range(1,5):
        print(f"kiválaszott fejlesztés: {lehetseges_fejl[fejlesztes_szama-1]}")
        break
