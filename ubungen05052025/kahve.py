kahveFiyatlari = {
    "espresso":2.50,
    "americano":3.00,
    "latte":2.50,
    "cappucino":3.00,
    "macchiato":2.50,
    "mocha":3.50,
    "flatwhite":2.50
}

sizeFiyatlari = {
    "medium":0,
    "large":1,
    "xl":1.50
}

durum = {
    "eatin":0,
    "takeaway":1
}

kahveMusteri = input("Hangi kahveyi istersiniz?: ")
sizeMusteri = input("Hangi boyutta olmasini istersiniz?: ")
durumMusteri = input("Eat-In veya Take away?: ")

print(f"{kahveMusteri.upper()} : {kahveFiyatlari[kahveMusteri]}£\n\t{sizeMusteri.upper()}\t{sizeFiyatlari[sizeMusteri]}£\n\t{durumMusteri.upper()}\t{durum[durumMusteri]}£\nOdemeniz gereken tutar: {kahveFiyatlari[kahveMusteri]+sizeFiyatlari[sizeMusteri]+durum[durumMusteri]}£")
