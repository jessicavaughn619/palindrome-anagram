# Take a scrambled word 'darra'
# Check if this word is an anagram of a palindrome.
# If yes, return True, if not return False

# Example - 'darra' => True
# Example - 'rca' => False

# Hint: pick multiple palindromes - odd and even length - check the frequency of letter appearances

# Palindrome examples - 'radar' 'toot' 'racecar' 'kayak', 'repaper', 'noon', 'anna'

def letter_frequency(word):
    frequency = {}
    for letter in word:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency

# Odd examples - all frequencies divisible by 2, one odd number allowed

# letter_frequency("repaper") => {'r': 2, 'e': 2, 'p': 2, 'a': 1}
# letter_frequency("racecar") => {'r': 2, 'a': 2, 'c': 2, 'e': 1}
# letter_frequency("kayak") => {'k': 2, 'a': 2, 'y': 1}


# Even examples - all frequencies are divisible by 2

# letter_frequency("toot") => {'t': 2, 'o': 2}
# letter_frequency("noon") => {'n': 2, 'o': 2}
# letter_frequency("anna") => {'a': 2, 'n': 2}

def check_anagram_of_palindrome(word):
    length = len(word)
    frequency = {}
    for letter in word:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    if length == 0:
        return True
    elif length % 2 == 0:
        for value in frequency.values():
            if value % 2 == 0:
                return True
            return False
    else:
        for value in frequency.values():
            print(value)
    return False

print(check_anagram_of_palindrome("radar"))