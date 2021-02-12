# write a function that generates a list of ints of 'n' length 
import random
import nltk
from nltk.corpus import words

def num_list(max_num, n):

    random_list = []
    
    for num in range(0,n):
        num = random.randint(0,max_num+1)
        random_list.append(num)
    
    random_list.sort()
    return random_list

def word_list(limit):
    
    random_list = random.sample(words.words(), limit)
    random_list.sort()
    return random_list