"""
3 edits, insert/delete/replace
given 2 strings check if 1 or 0 edits away

ex. pale -> ple = true
    pales -> pale = true
    pale -> bale = true
    pale -> bake = false
"""

# def inside(src = {}, trgt = {}):
#     # for key in src:
#     #     if key in trgt:
#     #         print key
#     #         if src[key] == trgt[key]:
#     #             print "has no more than 1 add and no more than 1 delete"
#     #             print "same number of letters so you should be good"
#     #         else:
#     #             print "keep a counter to see if it is replace"
#     #             print "too many changes"
#     #
#     #
#     # when inside the call that means
#     # there are just the right amount of characters
#     # now we need to check that at least 1 character is NOT the same
#
#     # ex. src = ab; trgt =  abc for addition
#     counter = 0
#     for key in src:
#         if key not in trgt:
#             counter += 1
#     if counter >= 1:
#         print "THEREs more than 1 change"
#     else:
#         print "you are okay"
#     return
#
# def checkEdit(str1, str2):
#     if str1 == str2:
#         print "0 edits away ;]"
#         return True
#     if len(str2) - len(str1) > 1:
#         print "has more than 1 add"
#         return False
#     if len(str2) - len(str1) < -1:
#         print "has more than 1 remove"
#         return False
#     # has only 1 plus, 1 minus, or same number
#     else:
#     # make sure that the rest of the string is the same
#     #     if the str1 is longer then swap the pass
#         if len(str1) > len(str2):
#             inside(str2, str1)
#         elif:
#             inside(str1, str2)
#         else:
#     #         they have equal length and can have counter threshold of >1
#
#     return
def inplace(str1, str2):
#     checks if all chars are the same
    flag = False
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            if(flag):
                return False
            flag = True
        i += 1
    return True

def check_rest(short, long):
# if short is not within long return false
    i = 0
    j = 0
    while i < len(short) and j < len(long):
        # make sure to iterate the long
        if short[i] != long[j]:
            # positions done equal
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True

def one_edit(str1, str2):
#     check if string are equal length
    if len(str1) == len(str2):
        # method that checks if all but 1 char is different
        return inplace(str1, str2)
    if abs(len(str1) - len(str2)) > 1:
        print "too many changes"
        return False
    # assign which is long and which is short
    if len(str1) > len(str2):
        long = str1
        short = str2
    else:
        long = str2
        short = str1

    return check_rest(short, long)

