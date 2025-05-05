container = [0.50,0.80]

musteriContainer = int(input("Kapta mi kulahta mi?[Kap icin 0][Kulah icin 1]: "))

musteriScoops = int(input("Kac top istersiniz?: "))

musteriSecenekler = {
    1:{1:0.40,
       0:0},
    2:{1:0.30,
       0:0},
    3:{1:0.60,
       0:0}
}
musteriSecenek1,MusteriSecenek2,MusteriSecenek3 = int(input("Misir gevregi ister misiniz?[Hayir icin 0][Evet icin 1]: ")), int(input("Cikolata serpmek ister misiniz?[Hayir icin 0][Evet icin 1]:")),int(input("Cilek ister misiniz?[Hayir icin 0][Evet icin 1]:"))

fatura = (container[musteriContainer]+(musteriScoops*1.0)+(musteriSecenekler[1][musteriSecenek1]+musteriSecenekler[2][MusteriSecenek2]+musteriSecenekler[3][MusteriSecenek3]))

print(f"{container[musteriContainer]} + {(musteriScoops*1)} + {musteriSecenekler[1][musteriSecenek1]} + {musteriSecenekler[2][MusteriSecenek2]} + {musteriSecenekler[3][MusteriSecenek3]}\nFaturanizin tutari: {fatura}p")