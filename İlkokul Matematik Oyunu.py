import random

print("Matematik Oyununa Hoş Geldiniz!")

while True:
    puan = 0
    deneme_hakki = 3

    for i in range(5):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
        if operator == "+":
            sonuc = a + b
        elif operator == "-":
            sonuc = a - b
        else:
            sonuc = a * b

        print(f"{i+1}. soru: {a} {operator} {b} = ?")
        cevap = input("Cevap: ")
        if cevap.isnumeric() and int(cevap) == sonuc:
            print("Tebrikler, doğru cevap!")
            puan += 10
        else:
            print("Maalesef, yanlış cevap.")
            deneme_hakki -= 1
            if deneme_hakki == 0:
                print("Deneme hakkınız bitti!")
                break

    print(f"Oyun bitti! Puanınız: {puan}")

    devam = input("Tekrar oynamak istiyor musunuz? (E/H) ")
    if devam.lower() != "e":
        break

print("Oyun bitti. Tekrar bekleriz!")
