"""
check if str2 is rotation of str1 with 1 call to is substring
ex. waterbottle is rotation erbottlewat
"""
import sys

def main(str1, str2):
    # print is_rotation(sys.argv[1], sys.argv[2])
    is_rotation(str1, str2)

def is_substring(src, trgt):
    return True

def is_rotation(str1, str2):
    print "HELLO"

    if len(str1) != len(str2):
        return False

#     rotation is when 2 parts of a rotated string are both substrings of string1
# for instance erbottle and wat are both substrings of waterbottle
#  hint about concat erbottlewat + erbottlewat = erbottlewaterbottle str1 and str2 are substrings
    mega = str1 + str1
    print mega
    if is_substring(str2, str1):
        return True
    return False

if __name__ == '__main__':

   main("waterbottle", "erbottlewat")