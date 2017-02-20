"""
module this time
check if string is in permutation of another

brute way is to store all perms of src and check if trgt is in it
runtime is O(n!)

runtime of below is O(n)
"""

def inPermu(src, trgt):
    # if same word
    # if src == trgt:
    #     return True
    # # same number of characters
    # if len(src) != len(trgt):
    #     return False
    # # same letters O(n)
    if sameLetters(src) != sameLetters(trgt):
        return False
    return True

def sameLetters(str):
    map = {}
    for ch in str:
        if ch in map:
            map[ch] += 1
        else:
            map[ch] = 1

    # print "\n"
    # print map
    return map

"""above uses space but can just use 1 table
    below we can sort both and compare"""

def sortBoth(src, trgt):
    if sorted(src) == sorted(trgt):
        return True
    return False