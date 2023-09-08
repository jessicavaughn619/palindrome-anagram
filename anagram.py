# Anagram - example: flute tufle, bored robed, study dusty, peach cheap
# bored - robbed 

# Check for frequency of letters in addition to whether the letters are all in each word

# If words are anagrams, return True, else return False

# How many letters are allowed - uppercase, lowercase, both?

# frequency_map[letter] = 0
# How to modify dict: dict[key] = value

def check_anagram(word1, word2):
    frequency_map = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        frequency_map[letter] = 0
    frequency1 = frequency_map.copy()
    for letter in word1:
        frequency1[letter] += 1
    frequency2 = frequency_map.copy()
    for letter in word2:
        frequency2[letter] += 1
    if frequency1 == frequency2:
        return True
    return False

# print(check_anagram("robed", "robbed"))


def check_anagram2(word1, word2):
    frequency1 = {}
    frequency2 = {} 
    for letter in word1: 
        if letter in frequency1:
            frequency1[letter] += 1
        else:
            frequency1[letter] = 1
    for letter in word2:
        if letter in frequency2:
            frequency2[letter] += 1
        else:
            frequency2[letter] = 1
    if frequency1 == frequency2:
        return True
    return False

# O(n + m)

# print(check_anagram2("", ""))

# Is this the first time this letter is occuring? 
# Check if in dict.keys()
# If letter is there, increment value += 1, but if not do something different