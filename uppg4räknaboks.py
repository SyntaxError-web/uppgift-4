# Program för att räkna antal vokaler i en text

# 1. Be användaren mata in en text
text = input("Mata in en text: ")

# 2. Sätt en räknare till 0
vokal_raknare = 0

# 3. Loopa genom varje tecken i texten
for tecken in text:
    # 4. Om tecknet är en vokal, öka räknaren med 1
    if tecken.lower() in "aeiou":
        vokal_raknare += 1

# 5. Skriv ut antalet vokaler
print(f"Antal vokaler i texten är: {vokal_raknare}")
