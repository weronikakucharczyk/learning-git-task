lista_zakupow={
    "piekarnia": ["chleb", "pączek", "bułki", "jagodzianki", "cynamonki"],
    "warzywniak": ["marchew", "seler", "rukola", "sałata", "pomidory"],
    "supermarket": ["mąka", "jajka", "mleko", "woda", "olej"]
}

suma_prod = 0

for sklep, produkty in lista_zakupow.items():
    sklep_wielka_lit = sklep.capitalize()
    produkty_wielka_lit = [produkt.capitalize() for produkt in produkty]
    print( f"Idę do {sklep_wielka_lit} i kupuję tam {produkty_wielka_lit}")

    suma_prod += len(produkty)
prod_supermkt = lista_zakupow["supermarket"]
produkty_str = ", ".join(prod_supermkt)

print(f"W sumie kupuję {suma_prod} produktów.")
print(f"Z produktów z supermarketu: ({produkty_str}) zrobię naleśniki")