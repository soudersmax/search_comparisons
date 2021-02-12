# write a function that generates a list of ints of 'n' length 
import random


def num_list(a,b):

    random_list = []
    
    for num in range(0,b):
        num = random.randint(0,a+1)
        random_list.append(num)
    
    random_list.sort()
    return random_list
