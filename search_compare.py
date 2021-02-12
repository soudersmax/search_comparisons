from lib.bin_search import bin_search
from lib.list_gen import num_list
from lib.lin_search import lin_search
from lib.timer import timed_function
import time


def run_search():
    ceil = int(input('What do you want the maximum to be? '))
    length = int(input('How long do you want your list? '))
    
    l1 = num_list(ceil,length)

    print(l1)
    
    target = int(input('What number do  you want to look for? '))

    go = input('Run search? (y/n) ')
    if go == 'y':
        print('\n')
        timed_function(bin_search, target, l1)
        print('\n')
        timed_function(lin_search, target, l1)
        print('\n')
        
    else:
        print('Nevermind!')

run_search()