class Osoba:  # třída pro osobu
    def __init__(self, jmeno:str, oblibeny_napoj:str, nalada:bool):  # konstruktor třídy Osoba
        self.jmeno = jmeno  # jméno osoby
        self.oblibeny_napoj = oblibeny_napoj  # oblíbený nápoj osoby
        self.nalada = nalada  # nálada osoby (šťastná/ smutná)
    def print_info(self):  # metoda pro výpis informací o osobě
        print(f"Jméno: {self.jmeno}, Oblíbený nápoj: {self.oblibeny_napoj}, Nálada: {self.nalada}")
    
class Kavarna:  # třída pro kavárnu
    def __init__(self, nazev:str, adresa:str):  # konstruktor třídy Kavarna
        self.nazev = nazev  # název kavárny
        self.adresa = adresa  # adresa kavárny
        self.zakaznici = []  # seznam zákazníků v kavárně
        self.nabidka = {"káva": 30, "čaj": 25, "espresso": 35}  # nabídka nápojů s cenami

    def pridat_zakaznika(self, osoba: Osoba):  # metoda pro přidání zákazníka do kavárny
        self.zakaznici.append(osoba)  # přidání osoby do seznamu zákazníků

    def print_zakaznici(self):  # metoda pro výpis všech zákazníků v kavárně
        for osoba in self.zakaznici:
            osoba.print_info()
    
    def objednej_napoj(self, osoba: Osoba, napoj: str):  # metoda pro objednání nápoje
        if napoj in self.nabidka:
            cena = self.nabidka[napoj]
            print(f"{osoba.jmeno} si objednal(a) {napoj} za {cena} Kč.")
            nalada_text = "šťastná" 
            print(f"Nálada zákazníka {osoba.jmeno} je nyní {nalada_text}.")
        else:
            print(f"Promiňte, {napoj} není v nabídce.")

    def objednej_napoj_od_uzivatele(self, osoba: Osoba):  # metoda pro interaktivní objednání nápoje od uživatele
        print(f"\nDobré dopoledne {osoba.jmeno}! Jaký nápoj byste si dali?")
        print("Dostupné nápoje:")
        for napoj, cena in self.nabidka.items():
            print(f"  - {napoj}: {cena} Kč")
        
        vyber = input("Zadejte název nápoje: ").lower().strip()
        
        if vyber in self.nabidka:
            cena = self.nabidka[vyber]
            print(f"\n{osoba.jmeno} si objednal(a) {vyber} za {cena} Kč.")
            osoba.nalada = True  # nálada se zlepší po objednání
            print(f"Nálada zákazníka {osoba.jmeno} je nyní šťastná ✓")
            return True
        else:
            print(f"\nPromiňte, '{vyber}' není v nabídce. Zkuste znovu.")
            return False

def main():
    kavarna = Kavarna("Cafe Praha", "Náměstí 1, Praha")  # vytvoření instance kavárny

    osoba1 = Osoba("Jan", "káva", True)  # vytvoření několika osob
    osoba2 = Osoba("Eva", "čaj", False)
    osoba3 = Osoba("Petr", "espresso", True)

    kavarna.pridat_zakaznika(osoba1)  # přidání osob do kavárny
    kavarna.pridat_zakaznika(osoba2)
    kavarna.pridat_zakaznika(osoba3)

    kavarna.objednej_napoj(osoba1, "vino")  # objednání nápojů
    kavarna.objednej_napoj(osoba2, "čaj")
    kavarna.objednej_napoj(osoba3, "espresso")

    # Interaktivní objednání nápoje od uživatele
    print("\n--- Interaktivní objednávka ---")
    kavarna.objednej_napoj_od_uzivatele(osoba1)

    print("\n--- Zákazníci v kavárně: ---")  # výpis všech zákazníků v kavárně
    kavarna.print_zakaznici()

if __name__ == "__main__":   # spuštění hlavní funkce
    main()