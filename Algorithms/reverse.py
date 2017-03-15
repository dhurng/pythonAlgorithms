"""
reverse a string
"""

def reverse(str):
    print str
    print str[::-1]

    print "***"
   
    counti = 0
    countj = len(str) - 1

    while counti < countj:

        i = str[counti]
        j = str[countj]

        temp = i
        i = j
        j = temp
        counti += 1
        countj -= 1

    print i
    print j
    print str
    
reverse("abcd")
