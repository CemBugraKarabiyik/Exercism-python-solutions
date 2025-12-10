def prime(number):

    asal_sayısı=0
    if number<1:
        raise ValueError('there is no zeroth prime')

    denenen_sayi=2 

    while True:
        if asal_mi(denenen_sayi):
            asal_sayısı+=1
            if asal_sayısı==number:
                return denenen_sayi
        denenen_sayi+=1

def asal_mi(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True