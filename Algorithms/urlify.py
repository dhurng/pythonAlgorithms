"""
Change all white spaces except for trailing to '%20'
Aside from Regex
"""
import re

def pythonReg(str):
    sol = re.sub(' ', '%20', str.rstrip())
    return sol

"""
strings are immutable meaning we creat a new string
space is just 1 string based on input O(n)
runtime of this would be O(n)
"""
def blackBox(str, trueLen):
    i = 0
    res = ''
    while i < trueLen:
        if str[i] == ' ':
            res += '%20'
        else:
            res += str[i]
        i += 1
    print res
    return