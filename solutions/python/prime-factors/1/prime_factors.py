def factors(value):
    divisior=2
    valueprimes=[]
    while value>1:
        while value%divisior==0:
            valueprimes.append(divisior)
            value//=divisior
        divisior+=1
    return valueprimes
    
            
