from lib.bin_search import bin_search
from lib.list_gen import num_list, word_list
from lib.lin_search import lin_search
from lib.timer import timed_function
import time


def run_search():
    list_type = input('Would you like to search strings or integers? (str/int) ')
    
    if list_type == 'int':
        
        max_num = int(input('What do you want the maximum to be? '))
        n = int(input('How long do you want your list? '))
        
        search_list = num_list(max_num,n)

        print(search_list)
        
        target = int(input('What number do  you want to look for? '))

    elif list_type == 'str':

        limit = int(input('How many words would you like in the list? '))
        search_list = word_list(limit)

        print(search_list)

        target = str(input('What word would you like to look for? '))

    else:
        print("Please enter 'str' or 'int'.")

    go = input('Run search? (y/n) ')
    if go == 'y':
        print('\n')
        timed_function(bin_search, target, search_list)
        print('\n')
        timed_function(lin_search, target, search_list)
        print('\n')
        
    else:
        print('Nevermind!')

run_search()