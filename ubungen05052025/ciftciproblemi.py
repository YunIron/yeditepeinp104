yumurtaMiktari = int(input("Bugun kac tane yumurta topladin?: "))

karton12 = yumurtaMiktari//12

karton6 = (yumurtaMiktari%12)//6

kahvalti = yumurtaMiktari - ((karton12*12)+(karton6*6))

print(f"Bugunki sonucunuz:\n12'li karton Yumurta adeti: [{karton12}]\n6'li karton Yumurta adeti: [{karton6}]\nKahvalti da yenilebilecek yumurta sayisi: [{kahvalti}]")