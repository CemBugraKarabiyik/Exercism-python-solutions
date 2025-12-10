def is_armstrong_number(number):

    str_num=str(number)
    basamak_sayisi = len(str_num)
    sum=0

    for rakam in str_num:
        sum+=int(rakam)**basamak_sayisi

    if sum ==number:
        return True
    else:
        return False

