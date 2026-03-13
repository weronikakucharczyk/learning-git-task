lista_zakupow={
    "piekarnia": ["chleb", "pączek", "bułki", "jagodzianki", "cynamonki"],
    "warzywniak": ["marchew", "seler", "rukola", "sałata", "pomidory"]
}

suma_prod = 0

for sklep, produkty in lista_zakupow.items():
    sklep_wielka_lit = sklep.capitalize()
    produkty_wielka_lit = [produkt.capitalize() for produkt in produkty]
    print( f"Idę do {sklep_wielka_lit} i kupuję tam {produkty_wielka_lit}")

    suma_prod += len(produkty)

print(f"W sumie kupuję {suma_prod} produktów.")