while True:
    yas = int(input("Yaşınızı daxil edin (dayandırmaq üçün 0): "))

    if yas == 0:
        print("Proqram dayandırıldı.")
        break
    elif yas < 0:
        print("Yaş mənfi ola bilməz!") 
    elif yas < 13:
        print("Siz yeniyetməsiniz.")
    elif yas < 18:
         print("Siz böyüksünüz.")
    else:
        print("Siz yaşlısınız.")