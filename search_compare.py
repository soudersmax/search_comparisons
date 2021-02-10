from bin_search import bin_search
from list_gen import num_list
from lin_search import lin_search
from timer import timed_function
import time


def run_search():
    ceil = int(input('What do you want the maximum to be? '))
    length = int(input('How long do you want your list? '))
    
    l1 = num_list(ceil,length)
    #l1 = [175, 190, 216, 405, 536, 749, 805, 1246, 1409, 1668, 1771, 1824, 2332, 2343, 
    #      2624, 2727, 3172, 3244, 3325, 3406, 3841, 3910, 3969, 4040, 4044, 4375, 4531, 
    #      5306, 5617, 5682, 5867, 5941, 6186, 6238, 6302, 6431, 6479, 6589, 6637, 6650,
    #      7064, 7534, 7585, 8044, 8483, 8513, 8647, 8932, 8973, 9143, 9196, 9405, 9411, 9566, 9770]
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