
# 1. Sätt startkapital till 100000
kapital = 100000

# 2. Läs in räntesats från användaren
ranta = float(input("Ange räntesats i procent (t.ex. 3.5): "))

# 3. Loopa över 5 år för att beräkna kapitalet år för år
for ar in range(1, 6):
    # Beräkna nytt kapital med ränta
    kapital = kapital * (1 + ranta / 100)
    # Skriv ut kapitalet för året med två decimaler
    print(f"År {ar}: {kapital:.2f} kr")

# 4. Avsluta programmet
print("Programmet är klart. Tack för att du använde räknaren!")