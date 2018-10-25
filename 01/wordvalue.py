from data import DICTIONARY, LETTER_SCORES
import string

def load_words():
    with open('dictionary.txt', 'r') as f:
        words = f.read().strip().split('\n')
    return words
    """Load dictionary into a list and return list"""
    pass

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    score = 0
    for char in word:
        if char in string.ascii_letters:
            score += int(LETTER_SCORES[char.upper()])
    return score

    

def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not word_list:
        word_list = load_words()
    biggest_word = ''
    high_score = 0
    for word in word_list:
        current_score = calc_word_value(word)
        if current_score > high_score:
            high_score = current_score
            biggest_word = word
    
    return biggest_word

if __name__ == "__main__":
    pass # run unittests to validate
