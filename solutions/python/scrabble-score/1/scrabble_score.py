def score(word):
    upperword=word.upper()
    points=0
    for char in upperword:
        if char in "AEIOULNRST":
            points+=1
        if char in "DG":
            points+=2
        if char in "BCMP":
            points+=3
        if char in "FHVWY":
            points+=4
        if char in "K":
            points+=5
        if char in "JX":
            points+=8
        if char in "QZ":
            points+=10
    return points
        
        
