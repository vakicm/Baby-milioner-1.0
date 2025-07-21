import random
import csv

class Pitanja:
    def __init__(self, pitanje, tacan_odg, odg1, odg2, odg3, odg4):
        """
        Pozvao sam konstruktor __init__ i nakon toga uveo argumente kako
        idu redom u fajlu pitanja.csv (pitanje, tacan_odg itd.) Kako bih
        pomesao sve
        """
        
        self._pitanje = pitanje
        self._tacan_odg = tacan_odg
        self._odgovori = [tacan_odg, odg1, odg2, odg3, odg4]
        random.shuffle(self._odgovori)
        self._osvojeni_iznos = 0
        

        """
        Fja za odgovore. Za svaki redni_br_odg u listi odgovori petlja ce prebrojati
        prethodno izmesane odgovore i pocece od prvog broja (start = 1)
        dok ce fja enumerati deliti redne brojeve od 1 do 5 svim odgovorima.
        Na primer:
        Pitanje: Glavni grad Srbije:
        1. Helsinki
        2. Tokio
        3. Beograd
        4. Vasington
        5. Pariz
        """        
    """
    def prik_odg(self)
        #Ova fja prikuplja odgovore izmedju 1 i 5.  
        #Ako nije izmedju 1 i 5, dize se ValueError da je unos neispravan i da mora da popravi.
        #Ako unese ok odgovor, fja vraca self._odgovori. kor_odg. - 1 stoji
        #zato sto je lista indeksirana od nule, pa ta -1 regulise da brojevi budu izmedju 1 i 5,
        #ukljucujuci te brojeve. Da imam samo return self._odgovori[kor_odg], Python
        #bi digao IndexError. Npr, da nema oduzimanja, kada bi korisnik uneo 1 pristupilo bi se
        #self_.odgovori[1], sto je drugi element u listi, a ne prvi kao sto bi trebalo, i tako u krug.
        #Na kraju funkcija vraca odgovor pomocu kog ce nastaviti dalje u igri.
    
    """               
   
    
    def nagrada(self, kor_odg, broj_pokusaja):
        """
        Spaja korisnikov odgovor sa poenima, ako odgovori tacno dobice 100 evra i ide dalje.
        Ako ne odgovori tacno ostaje na istoj svoti novca od malo pre ali gubi 1 zivot i dobice povratno
        obavestenje o preostalom broju zivota. Ako odgovori na sva pitanja dobija poruku x a ako izgubi sve zivote
        dize se error koji ga obavestava da vise nema zivota.
        """
        if kor_odg == self._tacan_odg:
            self._osvojeni_iznos += 100
            #print(f"Tačan odgovor! Idete talje! Trenutno imate {self._osvojeni_iznos} evra!")
    
        if kor_odg != self._tacan_odg:
            broj_pokusaja -= 1
            if broj_pokusaja == 1:
                print("Netačan odgovor! Ostao Vam je još 1 život. Pažljivo..")
            
            elif broj_pokusaja > 0:
                print(f"Netačan odgovor. Ostalo Vam je još {broj_pokusaja} zivota.")
            
            else:
                raise ValueError("Ostalo Vam je 0 zivota. Izgubili ste!")
        return self._osvojeni_iznos, broj_pokusaja
    
    def __str__(self):
        """
        Vraca pitanje u vidu stringa, poziva se kada se koristi print na klasi Pitanja.
        Neophodan kako bi fja radila kako treba.
        """      
        return(f"{self._pitanje}")


def ucitaj_pitanja_iz_csv(putanja= "pitanja.csv"):
    pitanja = []
    
    with open(putanja, "r", encoding="utf-8") as baza_pitanja:
        redovi = list(csv.reader(baza_pitanja))
        
        random.shuffle(redovi)    

        for red in redovi:
            if len(red) >= 7:
                pitanje = red[1]
                tacan_odg = red[2]
                odg1, odg2, odg3, odg4 = red[3:7]
                kviz = Pitanja(pitanje, tacan_odg, odg1, odg2, odg3, odg4)
                pitanja.append(kviz)
    return pitanja