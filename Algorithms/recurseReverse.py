"""
recursively reverse a string
"""

def recurse(string):
    print string
    
    if len(string) <= 1:
        return string

    return recurse(string[1:]) + string[0]

print recurse("abcd")
