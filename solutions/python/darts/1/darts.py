def score(x, y):
    uzakligin_karesi = x*x + y*y

    # 1. İç Çember (Yarıçap 1, Kare: 1*1=1)
    if uzakligin_karesi <= 1:
        return 10
    
    # 2. Orta Çember (Yarıçap 5, Kare: 5*5=25)
    # Zaten > 1 olduğu için, sadece <= 25 kontrolü yeterli
    elif uzakligin_karesi <= 25:
        return 5
        
    # 3. Dış Çember (Yarıçap 10, Kare: 10*10=100)
    # Zaten > 25 olduğu için, sadece <= 100 kontrolü yeterli
    elif uzakligin_karesi <= 100:
        return 1
        
    # 4. Hedefin Dışında
    else:
        # Orijinal kodunuzda burası boş bırakılmıştı, 0 puan döndürmelidir.
        return 0
