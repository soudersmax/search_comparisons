def lin_search(target,search_list):

    start = search_list[0]
    end = search_list[-1]

    if target < start or target > end:
        print(f'{target} is not in the list.')
        return None 

    for item in range(0,len(search_list)): 
        
        if target == search_list[item]:
            print(f'{target} is at index {item}.')          
            return item
        
        elif target < search_list[item]:
            print(f'{target} is not in the list.')
            return None

    print(f'{target} is not in the list.')
    return None

