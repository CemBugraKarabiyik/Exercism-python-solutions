def is_isogram(string):
    harfler=[]
    for i in string.lower():
        if i.isalpha():
            harfler.append(i)

    tekrarsiz_harfler=set(harfler)

    return len(tekrarsiz_harfler)==len(harfler)
        

