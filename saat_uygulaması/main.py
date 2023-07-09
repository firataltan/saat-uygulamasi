saat=int(input("saat:"))
dakika=int(input("dakika:"))
ekleme=int(input("eklenecek dakika:"))

saat=saat%24
dakika=dakika%60
yeni_saat=(saat+((dakika+ekleme)//60))%24
yeni_dakika=(dakika+ekleme)%60

print(f"{yeni_saat}:{yeni_dakika}")

