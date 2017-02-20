"""
Given a string
check if it is a permutation of a palindrome

ex. Tact Coa
    True (permutation: "taco cat, "atco cta", etc.)

Brute force find all permu
go through each permu and then check if pali

permu = same number of letters
pali = same letters on each end until mid
"""

# check if it can be a pali in the first place
# meaning it can only  have at least 1 char and rest is multiple of 2
#
# else false

def isPermuPali(str):
    # can probably lower it while going through list to save some time
    # str = str.lower()
    # or when iterating check if space, if space then do not add into map
    # str = str.replace(" ", "")

    print str

    if len(str) <= 1:
        return True

    # map all the characters
    map = {}
    for ch in str:
        ch = ch.lower()
        print ch
        if ch == " ":
            print "this is space and no map for you buddy"
            exit
        elif ch in map:
            map[ch] += 1
        else:
            map[ch] = 1
    print map

    # now check at least 1 key has odd value
    # and the rest of the keys have even values(mult of 2)

    counter = 0
    for i in map.values():
        print i
        print counter
        # this is an odd value
        if i % 2 != 0:
            counter += 1

        # exit condition cannot have more than 1 odd value
        if counter > 1:
            return False


        """please clean up ^ and also consider spaces and cases"""

    return True



