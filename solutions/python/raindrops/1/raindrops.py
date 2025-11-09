def convert(number):
    output=""
    if (int(number)%3==0):
        output+="Pling"
    if (int(number)%5==0):
        output+="Plang"
    if (int(number)%7==0):
        output+="Plong"
    if output=="":
        output=str(number)
    return output
