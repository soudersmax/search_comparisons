# write a function that generates a list of ints of 'n' length 
import random
from random_word import RandomWords

r = RandomWords()

def num_list(max_num, n):

    random_list = []
    
    for num in range(0,n):
        num = random.randint(0,max_num+1)
        random_list.append(num)
    
    random_list.sort()
    return random_list

def word_list(limit):

    word_list = None
    random_list = []
    
    while word_list is None:
        word_list = r.get_random_words(limit=limit)

    for word in word_list:
        lower_word= word.lower()
        random_list.append(lower_word)

    random_list.sort()
    #print(random_list)
    return random_list
