# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Ann Bozhenko
# Collaborators : <your collaborators>
# Time spent    : 3 days

import math
import random
import string
import functools

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.
    
    word: string
    n: int >= 0
    returns: int >= 0
    """
    # Count the amount of unique words.
    w_lower = word.lower()
    word_amount = dict()
    for char in w_lower:
        word_amount[char] = word_amount.get(char, 0) + 1 
    # Count first part.
    first_p = 0
    for char, value in SCRABBLE_LETTER_VALUES.items():
        if char in w_lower:
            first_p += value * word_amount[char]
    # Count second part.
    leng = len(word)
    sec_p = 7 * leng - 3 * (n - leng)
    if 1 > sec_p:
        sec_p = 1
    return first_p * sec_p


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line
    

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    for key in hand.keys():
        if key in VOWELS:
            hand['*'] = hand.pop(key)
            break

    return hand


def update_hand(hand, word):
    """
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)

    Run through evry key and value of copied hand and 
    subtract 1 from value if proper key was found in word.
    If subtraction gives negative number, the change is ignored.
    """
    # Form dictionary with unique letters and its values.
    hand_copy = hand.copy()
    w = word.lower()

    for letter in w:
        for char, value in hand_copy.items():
            if char == letter:
                difference = value - 1
                if difference < 0:
                    continue
                else:
                    hand_copy[char] = difference

    # Return filtered hand_copy (keys with value 0 are ignored).
    return {char: value for (char, value) in hand_copy.items() if value != 0}


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_lower = word.lower()
    word_dict = dict()
    # Create word dictionary, where the key is unique letter, its number in word is value.
    for letter in word_lower:
        word_dict[letter] = word_dict.get(letter, 0) + 1
    # Define possible vowels in hand key '*' if hand has '*'.
    all_vowels = [char for char in hand.keys() if char in VOWELS]
    wildcard_vowels = [char for char in VOWELS if char not in all_vowels]
    for key, value in word_dict.items():
        if key in hand.keys():
            difference = hand[key] - value
            if difference >= 0:
                if key == '*':
                    # Form word combinations and find out if possible word is in word_list.
                    wildcard_index = word.find('*')
                    for i in range(len(wildcard_vowels)):
                        possible_word = word_lower[:wildcard_index] + wildcard_vowels[i] + word_lower[wildcard_index + 1:]
                        if possible_word in word_list:
                            break
                        elif i == len(wildcard_vowels) - 1 and possible_word not in word_list:
                            return False
            else:
                return False
                
        else:
            return False
    
    # If no Falses were found, that means word is valid.
    return True


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    Uses reduce function in order to count sum of all values.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    numb = 0
    numb = functools.reduce(lambda v1, v2: v1 + v2, hand.values())
    return numb

def play_hand(hand, word_list):

    """
    hand: dictionary (string-> int)
    word_list: list of possible words

    Gets strings from user and shows the info about game status
    Returns a total score of a played hand game.
    """
    total_score = 0
    while True:
        if hand == {}:
            print('Ran out of letters')
            print(f'Total score for this hand: {total_score}')
            print('-------------------------------------------')
            break
        print('Current hand: ', end = '')
        display_hand(hand)
        word = input('Please enter a word or "!!" to indicate that you are finished: ')
        if word == '!!':
            print(f'Total score: {total_score}')
            break
        else:
            if is_valid_word(word, hand, word_list) == True:
                scores = get_word_score(word, calculate_handlen(hand))
                total_score += scores
                print(f'{word} earned {scores} points. Total: {total_score}')
                hand = update_hand(hand, word)
            else:
                hand = update_hand(hand, word)
                print('That is not a valid word. Please choose another word.')
                print()
        
    return total_score


def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    alphabet = VOWELS + CONSONANTS
    changed_hand = hand.copy()
    if letter in hand.keys():
        free_letters = [char for char in alphabet if char not in hand.keys()]
        random_l = random.choice(free_letters)
        changed_hand[random_l] = changed_hand.pop(letter)

    return changed_hand       
    

def play_game(word_list):
    """
    Uses a loop to check the validity of input data.
    Uses play_hand function to provide rounds of game.
    Uses inner loop to run through input number of rounds(hands_amount).

    word_list: list of lowercase strings
    """
    while True:
        try:
            hands_amount = int(input('Enter total number of hands: ')) 
            total_score = 0
            replay_try = 0
            for n in range(hands_amount):
                if n > 0 and replay_try < 1:
                    replay = input('Would you like to replay the hand? ')
                    if replay == 'yes':
                        total_score += play_hand(hand, word_list)
                        replay_try += 1                
                hand = deal_hand(HAND_SIZE)
                print('Current hand: ', end = '')
                display_hand(hand)
                wish_to_change = input('Would you like to substitute a letter? ')
                if wish_to_change == 'yes':
                    letter = input('Which letter would you like to replace: ')
                    hand = substitute_hand(hand, letter)
                print()
                score = play_hand(hand, word_list)
                total_score += score
            print(f'Total score over all hands: {total_score}')
            break
        except ValueError:
            print('Wrong format, try again!')
    

def change_hand_size():
    """
    This function is given a data if the user would like to change the size of hand
    and if they would then what number they wish. If user reject to change hand size then 
    the value of hand is not changed.
    """
    while True:
        try:
            change = input('Do you wish to change the size of hand, which is 7 unique letters (no/yes)? ')
            if change == 'yes':
                hand_size = int(input('What size: '))
                return hand_size
            break
        except ValueError:
            print('Wrong format, try again!')

    return HAND_SIZE
        

if __name__ == '__main__':
    word_list = load_words()
    HAND_SIZE = change_hand_size()
    play_game(word_list)
