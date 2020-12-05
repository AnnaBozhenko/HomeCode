import re
def func(my_word, other_word):
    # Create word string as my_word string without spaces.
    word = my_word.split(" ")
    word = "".join(word)
    # Create set of unique letters of my_word string.
    for_set = re.findall(r'[^_\s]', my_word)
    set_my_w = set(for_set)
    # Create set where letters from other_word will be stored.
    set_not_in_my_w = set()
    if len(word) == len(other_word):
        # Search the letters from other_word which corresspond to equivalent index letter "_" of word string.
        i = 0 
        while i < len(word):
            if word[i] == '_':
                set_not_in_my_w.union({other_word[i]})
                i += 1
            else:
                i += 1
                continue
        if set_my_w.issuperset(set_not_in_my_w) == True:
            return False
        else:
            i = 0
            count = 0
            while i < len(word):
                if word[i] == "_" or word[i] == other_word[i]:
                    count += 1
                    i += 1
                else:
                    i += 1
            if count == len(word):
                return True
            else:
                return False
    else:
        return False


def match_with_gaps(my_word, other_word):
    # Create word string as my_word string without spaces.
    word = my_word.split(" ")
    word = "".join(word)
    # Create set of unique letters of my_word string.
    for_set = re.findall(r'[^_\s]', my_word)
    set_original = set(for_set)
    set_differ = set()
    i = 0
    while i < len(word):
        if word[i] in set_differ:
            if word[i] == other_word[i]:
                i += 1
            else:
                set_differ.union({other_word[i]})
                i += 1
        else:
            return False
    if (set_original.union(set_differ) == set_original) == True:
        return True
    else:
        return False

test = match_with_gaps("a_ _ le", "apple")
print(test)