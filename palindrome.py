# Example: abba
# Establish two pointers, one at the beginning, one at the end
# While loop checking if the first pointer and second pointer are equal
# If not equal, return False, if equal, move to the next index
# If we do not find any disagreement, return True

example = "abba"
example2 = "radar"
example3 = "race car  "

# str.isalnum() check if number or letter
# str.isalpha() check if a-z
# str.isnumeric() check if 0-9

# Do not compare spaces or punctuation
def is_palindrome3(example: str) -> bool:
    length = len(example)
    first = 0
    last = length-1
    # punctuation = " ,.!?:;"
    while first < last:
        if not example[first].isalpha():
            first += 1
        elif not example[last].isalpha():
            last -= 1
        elif example[first] != example[last]:
            return False
        else:
            first += 1
            last -= 1
    return True

# Original
def is_palindrome(example: str) -> bool:
    length = len(example)
    first = 0
    last = length-1
    while first < last:
        if example[first] != example[last]:
            return False
        else:
            first += 1
            last -= 1
    return True

# Include spaces in comparison
def is_palindrome2(example: str) -> bool:
    length = len(example)
    first = 0
    last = length-1
    while first < last:
        while first < length and example[first] == " ":
            first += 1
        while last < length and example[last] == " ":
            last -= 1
        if example[first] != example[last]:
            return False
        else:
            first += 1
            last -= 1
    return True