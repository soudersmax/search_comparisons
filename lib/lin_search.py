# Write a linear search function with a timer
def lin_search(a,b):

    start = b[0]
    end = b[-1]
    i = 0
    
    if a < start or a > end:
        print(f'{a} is not in the list.')
        return None 

    while i in range(0, end):
        
        if a == b[i]:
            print(f'{a} is at index {i}.')          
            return i
        
        elif a > b[i]:
            i +=1
        
        else:
            print(f'{a} is not in the list.')
            return None

    print(f'{a} is not in the list.')
    return None

