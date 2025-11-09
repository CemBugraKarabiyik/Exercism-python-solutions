def is_pangram(sentence):
    harfler=[]
    eng_alphabet_length=26
    for i in sentence.lower():
        if i.isalpha():
            harfler.append(i)
    tekrarsiz_harfler=set(harfler)
    return len(tekrarsiz_harfler)==eng_alphabet_length
        
