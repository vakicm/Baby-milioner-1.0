import csv
import random

"""
Uloga ovog modula je da koristeći funkciju shuffle iz biblioteke random isčita pitanja iz csv dokumenta a potom
ih nasumično ređa kako bih proverio/poboljsao logiku kviza. Potpuno nepovezan sa druga 2 modula ali neka ostane, kao modul
odakle sam krenuo.
"""

with open("pitanja.csv", "r", encoding="utf-8" ) as baza_pitanja: #cita sve iz fajla pitanja i stavlja u promenljivu baza_pitanja
    sva_pitanja = list(csv.reader(baza_pitanja))
    
random.shuffle(sva_pitanja)

pitanja = [] #pravim listu za pitanja
for row in sva_pitanja[1:]: # preskace prvi cinilac (u slucaju pitanja.csv, preskace pocetni broj)
    pitanje = row[1] # identifikuje tekst nakon prvog zareza kao pitanje
    tacan_odg = row[2] # identifikuje tekst nakon drugog zareza kao tacan odgovor
    
    odg1, odg2, odg3, odg4 = row[3:] # ostali, netacni odgovori
    
user_odgovor = None # promenljivoj koja ce mi kasnije trebati zadajem trenutnu vrednost none tj nista
osvojeni_iznos = 0 # promenljivoj koja ce biti brojac novca koji sam osvojio dajem vrednost 0



# sad pravim fju za unos broja pitanja i unos broja pokusaja, ona ce koristiti while petlju koja ce se "vrteti" sve
# dok se ne ispune uslovi (broj pitanja >= 5 ili <= 20). ako se ispuni uslov za pitanja izlazi se iz petlje a ako se
# unese pogresni brojevi dize se else opcija. Ako se unese nesto skroz drugacije dize se drugi error.

while True:
    try:
        broj_pitanja = int(input("Unesite broj pitanja (izmedju 5 i 20): "))
        if broj_pitanja >= 5 and broj_pitanja <= 20 or broj_pitanja != int:
            break
        else:
            print("Uneli ste nedozvoljeni broj pitanja. Molim unesite dozvoljeni broj pitanja")
    except ValueError:
        print("Uneli ste nedozvoljeni karakter. Molim unesite dozvoljeni karakter.")
        

# isti princip kao malopre, beskonacna petlja koja ce se "vrteti" sve dok se ne ispune isti uslovi kao malo pre
# samo sa drugacijim brojevima (broj_pokusaja <=5 ili broj_pokusaja >= 20)

while True:
    try:
        broj_pokusaja = int(input("Unesite broj pokusaja (izmedju 5 i 20): "))
        if broj_pokusaja <= 5 and broj_pokusaja >= 20 or broj_pokusaja != int:
            break
        else:
            print("Uneli ste nedozvoljeni broj pitanja. Molim unesite dozvoljeni broj pitanja")
    except ValueError:
        print("Uneli ste nedozvoljeni karakter. Molim unesite dozvoljeni karakter.")