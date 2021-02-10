# Write a function called in_bisect that takes a sorted list and a target value and returns the index of the value in the list if it’s there, or None if it’s not.

def bin_search(a, b):
    
    end = len(b)
    mid =  end // 2
    index = mid
        
    # Check if item is in list
    if a < b[0] or a > b[-1]:
        print(f'{a} is not in the list.')     
        return None

    while mid >= 1:

        # Check for item
        if a == b[index]:
            print(f'{a} is at index {index}.')
            return index

        # Cut loop
        elif a > b[index]:
            mid = mid // 2
            index = min(index + mid + 1, end-1)
            #print(b[index:])

        elif a < b[index]:
            mid = mid // 2 
            index = max(index - mid - 1, 0)
            #print(b[new_index:index])
            #index = new_index

    # Check for item
    if a == b[index]:
        print(f'{a} is at index {index}.')        
        return index

    else:
        print(f'{a} is not in the list.')
        return None


