def find(search_list, value):
    search_list.sort()
    first,last=0,len(search_list)-1
    while first <= last:
        middle=(first+last)//2
        if search_list[middle]>value:
            last = middle - 1
        elif search_list[middle]<value:
            first = middle + 1
        else:
            return middle
        
    raise ValueError("value not in array")
        
    
