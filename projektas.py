v = input("iveskite savo varda")
p = input("iveskite savo pavarde")
m = int(input("iveskite savo amziu"))
u = float(input("iveskite savo ugi"))

vartotojo_informacija = {"vardas":v,"pavarde":p,"metai":m,"ugis":u}


print(f"Sveiki atvyke {vartotojo_informacija['vardas']}.")

pasirinkimas = int(input("iveskite pasirinkima:"
                         "1-pakeisti ugi"
                         "2-istrinti ugi"
                         "3-prideti svori"
                         "4-atspausdinti mano informacija"
                         "0-baigti programa"))

if pasirinkimas == 1:
    vartotojo_informacija["ugis"] = float(input("iveskite savo ugi"))
elif pasirinkimas == 2:
    del vartotojo_informacija["ugis"]
elif pasirinkimas == 3:
    vartotojo_informacija["svoris"] =float(input("iveskite savo svori"))
elif pasirinkimas == 4:
    print(f"vardas: {vartotojo_informacija['vardas']}"
          f"pavarde: {vartotojo_informacija['pavarde']}"
          f"metai: {vartotojo_informacija['metai']}"
          f"ugis: {vartotojo_informacija['ugis']}"
          f"svoris: {vartotojo_informacija['svoris']}")