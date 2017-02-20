"""
See if a string has only unique characters.
Try without extra data struct

"""

class Solution(object):
    def __init__(self):
        pass
#Hash Map
    def mapUniq(self, str):
        map = {}
        for ch in str:
            if ch in map:
                return False
            map[ch] = 1
        return True

#Bit Vector
    def bitVector(self, str):
        temp = 26
        if len(str) > temp:
            return False
        check = 0
        for ch in str:
            val = ord(ch) - ord('a')
            if check & (1 << val) > 0:
                return False
            else:
                check |= (1 << val)
        return True


    if __name__ == '__main__':
        print "Testing Unique"
        pass

