def bin_search(target, search_list):
    
    end = len(search_list)
    mid =  end // 2
    index = mid
        
    # Check if target is in list
    if target < search_list[0] or target > search_list[-1]:
        print(f'{target} is not in the list.')     
        return None

    while mid >= 1:

        # Check for target
        if target == search_list[index]:
            print(f'{target} is at index {index}.')
            return index

        # Cut loop
        elif target > search_list[index]:
            mid = mid // 2
            index = min(index + mid + 1, end-1)
            #print(b[index:])

        elif target < search_list[index]:
            mid = mid // 2 
            index = max(index - mid - 1, 0)
            #print(b[new_index:index])
            #index = new_index

    # Check for target
    if target == search_list[index]:
        print(f'{target} is at index {index}.')        
        return index

    else:
        print(f'{target} is not in the list.')
        return None