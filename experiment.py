
import string
def is_word_guessed(secret_word, letters_guessed):
    secret_word = secret_word.lower()
    letters_guessed_lower = [] 
    result = 0
    for element in letters_guessed:
        # Changing elements from letters_guessed list into lowercase.
        letters_guessed_lower.extend(element.lower())
     # Check if the elements in both list and secret_word are the same.
    for el in letters_guessed_lower: 
        for word in secret_word:
            if word == el:
                # Elements are the same.
                is_in_both = 1  
                # The sum of the same elements cases.
                result += is_in_both  
            else:
                # Elements are different.
                is_in_both = 0  
                # The sum of the same elements cases.
                result += is_in_both  
                # The sum of the same elements cases must be equal to the amount of words in secret_word.
    if len(secret_word) == result: 
        result = True
    else: 
        result = False
    return result


            
def get_guessed_word(secret_word, letters_guessed):
    # Change the type of letters_guessed variable into the string.
    letters_guessed = "".join(letters_guessed)
    # Form a set of characters from the string.
    letters_guessed = set(letters_guessed)
    guessed_word = list()
    # Run through the each character of secret_word and find the equivalent one in letters_guessed list.
    for char in secret_word:
        if char in letters_guessed:
            guessed_word.extend(char)
        else:
            guessed_word.extend("_")
    guessed_word = ' '.join(guessed_word)
    return guessed_word

'''a = get_guessed_word("apple", ["a", "p", "e", "", "l"])
print(a)'''  

def get_available_letters(letters_guessed):
    # Create a string of letters which are in letters_guessed list.
    letters_guessed = ''.join(letters_guessed)
    # Create a set of letters which are not in letters_guessed list.
    not_letters_guessed = set(string.ascii_lowercase) - set(letters_guessed)
    # Turn th type of not..guessed variable into string
    not_letters_guessed = ''.join(not_letters_guessed)
    return not_letters_guessed

'''b = get_available_letters(['e', 'i', 'k', 'p', 'r', 's'])
print(b)
print(set('abcdfghjlmnoqtuvwxyz') == set(b))'''

def hangman(secret_word):

    print('Wellcome to the Hangman!')
    length_word = len(secret_word)
    print(f'I am thinking of a word that is {length_word} letters long.')
    warnings_remaining = 3
    print(f'You have {warnings_remaining} warnings left.')
    guesses_remaining = 6
    letters_guessed = list()

    while guesses_remaining >= 0 or is_word_guessed(secret_word, letters_guessed) == True:
        print('---------------')
        print(f'You have {guesses_remaining} guesses left.')
        available_letters = get_available_letters(secret_word)
        print(f'available_letters: {available_letters}')
        guess = input("Please guess a letter:")
        guess = guess.lower()
        if guess.isalpha() is True and guesses_remaining > 0:
            if guess in letters_guessed:
                if warnings_remaining >= 0:
                    print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left:")
                    warnings_remaining -= 1
                    print(f'{get_guessed_word(secret_word, letters_guessed)}')
                    continue
                else:
                    print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess:")
                    guesses_remaining -= 1
                    print(f'{get_guessed_word(secret_word, letters_guessed)}')
                    continue
            elif guess in secret_word:
                letters_guessed.extend(guess)
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                is_word_guessed(secret_word, letters_guessed)
                continue
            elif guess in set('aeoui'):
                    print('Oops! That letter is not in my word.')
                    guesses_remaining -= 2
                    continue
            else:
                print('Oops! That letter is not in my word.')
                guesses_remaining -= 1
                continue
        else:
            if warnings_remaining >= 0:
                    print(f"That is not a valid letter. You have {warnings_remaining} warnings left:")
                    warnings_remaining -= 1
                    print(f'{get_guessed_word(secret_word, letters_guessed)}')
                    continue
            else:
                print(f"That is not a valid letter. You have no warnings left so you lose one guess:")
                guesses_remaining -= 1
                print(f'{get_guessed_word(secret_word, letters_guessed)}')
                continue
    if is_word_guessed(secret_word, letters_guessed) == True:
        unique_words = set(secret_word)
        unique_words = "".join(unique_words)
        score = (6 - warnings_remaining)*len(unique_words)
        return print(f"Congratulations, you won! Your total score for this game is: {score}")
    else:
        return print(f'Sorry, you ran out of guesses. The word was {secret_word}')
hangman('apple')




    


