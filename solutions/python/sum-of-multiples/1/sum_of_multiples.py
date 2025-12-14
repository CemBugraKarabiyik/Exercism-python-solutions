def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    for i in range(1,limit):
        for bolme in multiples:
            if bolme != 0 and i%bolme==0:
                unique_multiples.add(i)
            
    return sum(unique_multiples)
            
