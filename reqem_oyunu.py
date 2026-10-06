import random

print("Rəqəm Təxmininə xoş gəlmisiniz!")
dogru_reqem = random.randint(1, 100)
sayi = 0

while True:
    sayi += 1
    təxmin = int(input(f"{sayi}. təxmininizi daxil edin: "))
    
    if təxmin < dogru_reqem:
        print("Təxmininiz kiçikdir. Daha böyük bir rəqəm təxmin edin!")
    elif təxmin > dogru_reqem:
        print("Təxmininiz böyüktür. Daha kiçik bir rəqəm təxmin edin!")
    else:
        print(f"Təbrik edirəm! Rəqəmi tapdınız: {dogru_reqem}")
        break
