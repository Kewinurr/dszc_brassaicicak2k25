import random
projekt_azon = [int(5)]
projekt_nev = [str("öt")]
projekt_koltseg = [int(5)]
projekt_kezdodatum = [int("5")] #valamilyen dátum idk
projekt_befejeződatum = [int("5")] #valamilyen dátum idk
projekt_erintettepuletek = [str("épület neve")]


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
penzkeret = int(input("MAX pénz összeg a városban zajló fejlesztésekre: "))


#Épületek adatainak kiegészítése egy jelzővel (pl. jó, vagy 1-5-ös skálán) [STRING/INT], ha már megvan a CSV fájlunk.
#Szolgáltatások havi költsége, ha már megvan a CSV fájlunk

while True:
    fejlesztes_szama = int(input("\nFejlesztési döntések (A fejlesztése döntések számának a beírásával választod ki.)\n\t1. Új épület építése\n\t2. Karbantartás meglévő épületen\n\t3. Új szolgáltatás bevezetése\n\t4. Szolgáltatás megszüntetése\nVálassz egyet: "))
    if fejlesztes_szama in range(1,5):
        break